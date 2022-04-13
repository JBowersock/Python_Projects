class Example: # assigning a class.
    def __init__(self): #defining a function.
        self.__privateVar = 8 #assigned a value.

    def getExample(self): #defining a function.
        print(self.__privateVar) #prints value above.

    def setExample(self,private): #defining a function.
        self.__privateVar = private #changing to private.

obj = Example() #calling the parent function.
obj.getExample() #calling the child function 'getExample', which prints the value above.
obj.setExample(12) #callng the child function 'setExample', assigning a new value of 12.
obj.getExample() #calling the child function 'getExample' again, demonstrating the value has changed.
