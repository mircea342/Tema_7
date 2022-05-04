# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

from abc import abstractmethod

class FormaGeometrica:
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print(f"Cel mai probabil am colturi")

# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.__latura = latura

# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de interfata

    def get_latura(self):
        return self.__latura

    def set_latura(self,latura_dorita):
        self.__latura = latura_dorita

    def delete_latura(self):
        del self.__latura

    def aria(self):
        return f"Aria patratului este {self.__latura*self.__latura}"

# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self,raza_dorita):
        self.__raza = raza_dorita

    def delete_raza(self):
        del self.__raza

    def aria(self):
        return f"Aria cercului este {self.__raza*FormaGeometrica.PI}"

    # POLYMORPHISM

    # Definiti o noua metoda descrie - printati ‘Eu nu am colturi’

    def descrie(self):
        print(f"Eu nu am colturi")

P1 = Patrat(5)

P1.descrie()
print(P1.get_latura())
P1.delete_latura()
P1.set_latura(8)
print(P1.get_latura())
print(P1.aria())

print("===============================================================================================")
C1 = Cerc(3)

C1.descrie()
print(C1.get_raza())
C1.delete_raza()
C1.set_raza(8)
print(C1.get_raza())
print(C1.aria())






