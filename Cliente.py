import Pyro4
import time
from LamportClock import LamportClock

class Cliente:
    def __init__(self, id):
        self.id = id
        self.lamport_clock = LamportClock()
        self.barbeiro = Pyro4.Proxy("PYRONAME:barbeiro")

    def cortarCabelo(self):
        self.lamport_clock.increment()
        cont = self.lamport_clock.get_time()
        self.barbeiro.entrarNaRegiaoCritica(self.id, "cabelo", cont)

    def cortarBarba(self):
        self.lamport_clock.increment()
        cont = self.lamport_clock.get_time()
        self.barbeiro.entrarNaRegiaoCritica(self.id, "barba", cont)

    def cortarBigode(self):
        self.lamport_clock.increment()
        cont = self.lamport_clock.get_time()
        self.barbeiro.entrarNaRegiaoCritica(self.id, "bigode", cont)

clientes = [Cliente(i) for i in range(1, 6)]

for i in range(20):
    clientes[0].cortarCabelo()
    clientes[1].cortarBarba()
    clientes[2].cortarBigode()
    clientes[3].cortarCabelo()
    clientes[4].cortarBarba()
    time.sleep(1) 
