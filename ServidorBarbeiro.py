import threading
import time
import Pyro4
from LamportClock import LamportClock

@Pyro4.expose
class ServidorBarbeiro(object):
    def __init__(self):
        self.lamport_clock = LamportClock()
        self.lock = threading.Lock()
        self.current_client = None
        
    def cortarCabelo(self):
        print("Iniciando corte de cabelo...")
        self.lamport_clock.increment()
        time.sleep(3)
        print("Corte de cabelo finalizado.")
        self.lamport_clock.increment()
        
    def cortarBarba(self):
        print("Iniciando corte de barba...")
        self.lamport_clock.increment()
        time.sleep(4)
        print("Corte de barba finalizado.")
        self.lamport_clock.increment()
        
    def cortarBigode(self):
        print("Iniciando corte de bigode...")
        self.lamport_clock.increment()
        time.sleep(5)
        print("Corte de bigode finalizado.")
        self.lamport_clock.increment()
        
    def carimboDeTempo(self):
        return self.lamport_clock.get_time()
    
    @Pyro4.oneway
    def entrarNaRegiaoCritica(self, client_id, rc, timestamp):
        with self.lock:
            self.lamport_clock.clock = max(self.lamport_clock.clock, timestamp) + 1
      
            if self.current_client is not None and self.current_client != client_id:
                print(f"Cliente {client_id} aguardando para utilizar o recurso {rc}")
                return
            
            self.current_client = client_id
            print(f"Cliente {client_id} utilizando o recurso {rc}")
            
            if rc == "cabelo":
                self.cortarCabelo()
            elif rc == "barba":
                self.cortarBarba()
            elif rc == "bigode":
                self.cortarBigode()
                
            self.current_client = None
            print(f"Cliente {client_id} liberou o recurso {rc}")
    
    @Pyro4.oneway
    def concorrer(self, client_id, rc, timestamp):
        self.entrarNaRegiaoCritica(client_id, rc, timestamp)

if __name__ == "__main__":
    with Pyro4.Daemon() as daemon:
        barbeiro = ServidorBarbeiro()
        uri = daemon.register(barbeiro)
        ns = Pyro4.locateNS()
        ns.register("barbeiro", uri)
        print("URI do servidor:", uri)
        print("Servidor em Execução...")
        daemon.requestLoop()