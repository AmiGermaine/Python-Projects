#Parent Class user
class Food:
    nutrient = "Protein"
    calories = "4 calories per gram"
    benefit = "Repair"

    def getFood(self):
        print("That is a good source of, {}!".format(Food.nutrient))
        print("You can also try this if you're vegan.")

#Child Class Vegetables
class Vegetable(Food):
    color = "Green"
    taste = "Spicy"
    texture = "Crunchy"

    def getFood(self):
        print("It is very, {}!".format(Vegetable.taste))
        print("Try to eat more nuts too.")

#Another Child Class chicken
class Chicken(Food):
    smell = "Aromatic"
    touch = "Firm"

    def getFood(self):
        print("So {}!".format(Chicken.smell))
        print("Don't forget to drink water.")



#The following code invokes the methods inside each class for food, vegetable and chicken.

body = Food()
body.getFood()

diet = Vegetable()
diet.getFood()

eat = Chicken()
eat.getFood()