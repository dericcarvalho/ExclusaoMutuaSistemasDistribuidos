import time
import Pyro4
from LamportClock import LamportClock

@Pyro4.expose
class Barbeiro(object):
    def __init__(self):
        self.lamport_clock = LamportClock()
        
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
