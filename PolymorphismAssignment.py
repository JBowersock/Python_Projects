class Norse: #parent class
    name = 'Unknown'
    nickname = 'Unknown'
    animal = 'Unknown'
    weapon = 'Unknown'
    
    def information(self):
        msg = "\nName: {}\nNickname: {}\nAnimal: {}\nWeapon: {}".format(self.name,self.nickname,self.animal,self.weapon)
        return msg

class Thor(Norse): #child class one
    name = 'Thor'
    nickname = 'God of Thunder'
    animal = 'Goat'
    weapon = 'Hammer'
    hair_color = 'blonde' #individual attribute 1
    favorite_game = 'Fortnite' #individual attribute 2

    def favorite(self):
        msg = "The mighty Thor has {} hair and enjoys {} in his spare time.".format(self.hair_color,self.favorite_game)
        return msg

class Loki(Norse): #child class two
    name = 'Loki'
    nickname = 'God of Mischief'
    animal = 'Wolf'
    weapon = 'Staff'
    personality = 'mischievous' #individual attribute 1
    dislikes = 'lightning' #individual attribute 2

    def dislike(self):
        msg = "Loki is a bit on the {} side, and strongly dislikes {}.".format(self.personality,self.dislikes)
        return msg

if __name__ == "__main__":
    thor = Thor()
    print(thor.information())
    print(thor.favorite())

    loki = Loki()
    print(loki.information())
    print(loki.dislike())   

##POLYMORPHISM SUBMISSION ASSIGNMENT
##
##Create two classes that inherit from another class.
##
##Each child should have at least two of their own attributes.
##
##The parent class should have at least one method (function).
##
##Both child classes should utilize polymorphism on the parent class method.
##
##Add comments throughout your Python explaining your code.
