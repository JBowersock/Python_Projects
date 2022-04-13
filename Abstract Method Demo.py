from abc import ABC, abstractmethod #importing the abstract method.
class One(ABC): #parent class
    def money(self,amount): #defining function.
        print("Your total today is: $",amount) #regular method. #prints string.

    def dinero(self,amount): #defining function.
        pass #abstract method.

class Two(One): #child class
    def dinero(self,amount): #defining function. how to implement the parent class function 'dinero'.
        print('Hey, there\'s ${}!'.format(amount)) #prints string and value.

obj = Two() #assigned function to a variable.
obj.money("125") #calling parent function 'money', gave value.
obj.dinero("250") #calling shared function, gave value.
