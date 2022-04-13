#Protected & Private Variables Demo

class Example: # assigning a class.
    def __init__(self): #defining a function.
        self.__privateVar = 8 #assigned a value.

    def getExample(self): #defining a function.
        print(self.__privateVar) #prints value above.

    def setExample(self,private): #defining a private function.
        self.__privateVar = private #changing to private.

    def protectEx(self): #defining a protected function.
        self._protectedVar = 0 #assigned a value.

obj = Example() #calling the function.
obj.getExample() #calling the function 'getExample', which prints the value above.
obj.setExample(12) #callng the function 'setExample', assigning a new value of 12.
obj.getExample() #calling the function 'getExample' again, demonstrating the value has changed.
obj._protectedVar = 34 #calling the function 'protectEx', assigned new value of 34.
print(obj._protectedVar) #print protected variable, otherwise wont display.
