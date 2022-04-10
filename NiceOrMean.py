#This Nice or Mean Game was finished in Python Course Step 202

def start(nice=0,mean=0,name=""): #defining a function with parameters. note: nice and mean recieve index values, while name is a string value.
    # get user's name
    name = describe_game(name) #assigned a function with parameter to a variable called 'name'.
    nice,mean,name = nice_mean(nice,mean,name) #assigned 3 variables to a function called 'nice_mean' with parameters..
    #by doing it the way about you're getting information from and putting information back into the function.

def describe_game(name): #defining a function with a parameter.
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name.
    if name != "": #If name is not equal to empty.
        print("\nThank you for playing again, {}!".format(name)) #Print string and name input.
    else:
        stop = True #Stop asking for name.
        while stop: #While stop is true.
            if name == "": #If 'name' is equal to empty.
                name = input("\nWhat is your name? \n>>> ").capitalize() #Asks user their name and then capitalizes it.
                if name != "": #If 'name' is NOT empty.
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False #Inserts boolean value False into 'stop', ending the cycle.
    return name #takes the users name inputed, then passes the result to the code block above (def start)'s 'name'.

def nice_mean(nice,mean,name):
    stop = True #Variable 'stop' with a boolean value 'True'.
    while stop: #While stop is true.
        show_score(nice,mean,name) #Created function 'show_score' which contains variable values.
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n": #If user picks 'n' (for nice).
            print("\nThe stranger walks away smiling...") #Prints string when user picks 'n'.
            nice = (nice +1) #Gives score a plugin value of 1.
            stop = False #Stop asking user, loop is finished.
        if pick == "m": #If user picks 'm' (for mean).
            print ("\nThe stranger glares at you \nmenacingly and storms off\n shouting to the heavens!") #Prints string when user picks 'm'.
            mean = (mean + 1) #Gives score a plugin value of 1.
            stop = False #Stop asking user, loop is finished.
    score(nice,mean,name) #Passes the 3 variables to the score() function.

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean)) #The reason these values are ordered this way, is because of the string! Take a look.

def score(nice,mean,name):
        #Score function is being passed the values stored within the 3 variables.
        if nice > 2: #If condition is valid, call win function passing in the variables so it can use them.
            win(nice,mean,name)
        if mean > 2: #If condition is valid, call lose function passing in the variables so it can use them.
            lose(nice,mean,name)
        else:        #Else, call nice_mean function passing in the variables so it can use them.
            nice_mean(nice,mean,name)

def win(nice,mean,name):
    #Substitute the {} Wildcards with our variable values.
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #Call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #Substitute the {} Wildcards with our variable values.
    print("\nAhhh to bad, game over!, \nyou live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #Call again function and pass in our variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nThanks for playing. Come again!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'Yes', ( N ) for 'No':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, i do not reset the name variable as that same user has elected to play again.
    start(nice,mean,name)



if __name__ == "__main__":
    start()
