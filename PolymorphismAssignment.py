class Odin: #parent class
    name = "Unknown"
    mythology = 'Norse'
    classification = 'God'
    
    def information(self): #parent class function.
        msg = "Mythology: {}\nClassification: {}\n".format(self.mythology,self.classification)
        return msg

class Thor(Odin): #child class
    name = 'Thor' 
    hair_color = 'Blonde' #individual attribute 1
    favorite_game = 'Fortnite' #individual attribute 2

    def samename(self): #child class function.
        msg = "Name:  {}\nHair Color: {}\nFavorite Game: {}".format(self.name,self.hair_color,self.favorite_game)
        return msg

class Loki(Odin): #child class
    name = 'Loki'
    personality = 'Mischievous' #individual attribute 1
    dislikes = 'Lightning' #individual attribute 2

    def samename(self): #child class function.
        msg = "Name: {}\nPersonality: {}\nDislikes: {}".format(self.name,self.personality,self.dislikes)
        return msg

if __name__ == "__main__":
    thor = Thor()
    print(thor.samename())
    print(thor.information())

    loki = Loki()
    print(loki.samename())
    print(loki.information())


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
