class Kämpfer:
    def __init__(self,name,age,food):
        self.name = name
        self.age = age
        self.food = food

    def Spruch(self):
        print(f"Ich bin {self.name}, bin {self.age + 10} Jahre alt und mein Lieblingsessen sind {self.food}")

Johannes = Kämpfer("Johannes",33,"Bananen")
Justus = Kämpfer("Justus",21,"Geldscheine")
Jonathan = Kämpfer("Jonathan",11,"Ananas")

Johannes.Spruch()
Justus.Spruch()
Jonathan.Spruch()