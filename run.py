class Ninja:

    def __init__(self, first_name, last_name, treats, food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.food = food
        self.pet = pet 

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.food) > 0:
            food = self.food.pop()
            print(f"Let's feed you {self.pet.name} {food}")
        else: 
            print("Sorry, you ran out of food")
        return self

    def bathe(self):
        self.pet.noise()

class Pet:
    def __init__(self, name, type, tricks, noise): 
        self.name= name 
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50
    
    def sleep(self):
        self.energy +=25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self 

    def play(self):
        self.health += 5
        self.energy -= 15
        return self 

    def noise(self):
        print(self.noise)

treats = ['Banana', 'Apple', 'Carrots']
food = ['Tacos', 'Pizza', 'Kibble']

max = Pet("Max is a  dog from Mississippi")
pablo = Ninja("Pablo loves Max",treats, food, max)

pablo.feed()

