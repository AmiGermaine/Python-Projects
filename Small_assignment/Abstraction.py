
from abc import ABC,abstractmethod

# Abstraction class
class Animal(ABC):
    def eat(self): # regular method
        print('This cat like to eat tuna!')
    @abstractmethod
    def favoriteSnack(self):
        pass

# abstract method inherited from parent(Animal)
class Dog(Animal):
    def favoriteSnack(self):
        print('Love pup-peroni')

class Rabbit(Animal):
    def favoriteSnack(self):
        print('carrots')  

class Turkey(Animal):
    def favoriteSnack(self):
        print('kale') 

# 

pet = Dog()
pet.favoriteSnack()
pet.eat()
food = Turkey()
food.favoriteSnack()

cute = Rabbit()
cute.favoriteSnack()

