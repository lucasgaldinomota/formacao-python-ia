from abc import ABC, abstractmethod


class Atendente(ABC):
    @abstractmethod
    def saudacao(self):
        pass


class AtendentePt(Atendente):
    def saudacao(self):
        return "Bom dia"


class AtendenteEn(Atendente):
    def saudacao(self):
        return "Good Morning"


class AtendenteJp(Atendente):
    def saudacao(self):
        return "おはよう"


a1 = AtendenteEn()
print(a1.saudacao())

a1 = AtendenteJp()
print(a1.saudacao())
