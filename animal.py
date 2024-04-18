class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("o animal faz algum som")
        
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca= raca
        
    def fazer_som(self):
        print("o cachorro fez au au")
animal_generico = Animal(input("digite o nome de um animal: "))
cachorro1 = Cachorro("rex", "labrador")
animal_generico.fazer_som()
cachorro1.fazer_som()
