#Encountering one issue. Where when user loses, and are asked to replay. If they select yes, the game crashes.

def start(prize=0,name=""):
    name = describe_game(name)
    prize = q1(prize,name),q2(prize,name),q3(prize,name),q4(prize,name),q5(prize,name),q6(prize,name),q7(prize,name),q8(prize,name),q9(prize,name),q10(prize,name),q11(prize,name),q12(prize,name),q13(prize,name),q14(prize,name),q15(prize,name)

def describe_game(name):
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nBefore we begin, what is your name? \nName: ").capitalize()
                if name != "":
                    print("\nWelcome to Who Wants to Be A Millionaire, {}!".format(name))
                    print("\nLadies and gentleman. Here we go!")
                    stop = False
    return name

def q1(prize,name): #Question 1.
    stop = True
    while stop:
        print("\n#1. A magnet would most likely attract which of the following?")
        print("A. Metal")
        print("B. Plastic")
        print("C. Wood")
        print("D. Paper")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "a":
            print("\nThat is correct!")
            stop = False
        if pick != "a":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            stop = False
            lose(prize)

def q2(prize,name): #Question 2.
    stop = True
    while stop:
        show_score(prize+100)
        print("\n#2. In the United States, what is traditionally the proper way to address a judge?")
        print("A. Your holiness")
        print("B. Your honor")
        print("C. Your eminence")
        print("D. You the man!")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "b":
            print("\nThat is correct!")
            stop = False
        if pick != "b":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q3(prize,name): #Question 3.
    stop = True
    while stop:
        show_score(prize+200)
        print("\n#3. Where did Scotch whisky originate?")
        print("A. Ireland")
        print("B. Wales")
        print("C. Germany")
        print("D. Scotland")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "d":
            print("\nThat is correct!")
            stop = False
        if pick != "d":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q4(prize,name): #Question 4.
    stop = True
    while stop:
        show_score(prize+300)
        print("\n#4. The popular children's song \"It's Raining, It's Pouring\" mentions an \"old man\" doing what?")
        print("A. Snoring")
        print("B. Cooking")
        print("C. Laughing")
        print("D. Yelling")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "a":
            print("\nThat is correct!")
            stop = False
        if pick != "a":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q5(prize,name): #Question 5.
    stop = True
    while stop:
        show_score(prize+500)
        print("\n#5. If someone asked to see your ID, what might you show them?")
        print("A. Your tongue")
        print("B. Your teeth")
        print("C. Your passport")
        print("D. The door")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "c":
            print("\nThat is correct!")
            stop = False
        if pick != "c":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q6(prize,name): #Question 6.
    stop = True
    while stop:
        show_score(prize+1000)
        print("\n#6. According to a common phrase, a person who takes chances is \"going out on a\" what?")
        print("A. Horse")
        print("B. Limb")
        print("C. Skateboard")
        print("D. Nude Beach")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "b":
            print("\nThat is correct!")
            stop = False
        if pick != "b":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q7(prize,name): #Question 7.
    stop = True
    while stop:
        show_score(prize+2000)
        print("\n#7. Due to the geographical areas they represented, the opposing sides of the US Civil War were known by what names?")
        print("A. The Hills and the Valleys")
        print("B. The Cities and the Farms")
        print("C. The North and the South")
        print("D. The Boys and Girls")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "c":
            print("\nThat is correct!")
            stop = False
        if pick != "c":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q8(prize,name): #Question 8.
    stop = True
    while stop:
        show_score(prize+4000)
        print("\n#8. A geologist would likely be least helpful for answering questions about which of the following?")
        print("A. Granite boulders")
        print("B. Precious stones")
        print("C. Igneous rocks")
        print("D. Fruity Pebbles")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "d":
            print("\nThat is correct!")
            stop = False
        if pick != "d":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q9(prize,name): #Question 9.
    stop = True
    while stop:
        show_score(prize+8000)
        print("\n#9. According to the old saying, \"love of\" what \"is the root of all evil\"?")
        print("A. Food")
        print("B. Money")
        print("C. Clothing")
        print("D. Television")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "b":
            print("\nThat is correct!")
            stop = False
        if pick != "b":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q10(prize,name): #Question 10.
    stop = True
    while stop:
        show_score(prize+16000)
        print("\n#10. When a man is rudely ignored, he is said to be getting what?")
        print("A. Hot knee")
        print("B. Warm toe")
        print("C. Cold shoulder")
        print("D. His car fixed")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "c":
            print("\nThat is correct!")
            stop = False
        if pick != "c":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q11(prize,name): #Question 11.
    stop = True
    while stop:
        show_score(prize+32000)
        print("\n#11. A person who is not a banker and lends money at an extremely high interest rate is known as what?")
        print("A. Loan shark")
        print("B. Green snake")
        print("C. Paper tiger")
        print("D. Brother-in-Law")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "a":
            print("\nThat is correct!")
            stop = False
        if pick != "a":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q12(prize,name): #Question 12.
    stop = True
    while stop:
        show_score(prize+64000)
        print("\n#12. A common piece of advice goes \"be there or be\" what?")
        print("A. Bare")
        print("B. Square")
        print("C. Aware")
        print("D. Alone")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "b":
            print("\nThat is correct!")
            stop = False
        if pick != "b":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q13(prize,name): #Question 13.
    stop = True
    while stop:
        show_score(prize+125000)
        print("\n#13. Where would you most likely hear the request \"Cleanup in aisle 5\"?")
        print("A. Karate Class")
        print("B. Supermarket")
        print("C. Kindergarten")
        print("D. Drive-thru")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "b":
            print("\nThat is correct!")
            stop = False
        if pick != "b":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q14(prize,name): #Question 14.
    stop = True
    while stop:
        show_score(prize+250000)
        print("\n#14. If you're trying to find other players in a game of hide-and-seek, what are you most likely called?")
        print("A. Butterbean")
        print("B. Stinky")
        print("C. Dunce")
        print("D. It")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "d":
            print("\nThat is correct!")
            stop = False
        if pick != "d":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def q15(prize,name): #Question 15.
    stop = True
    while stop:
        show_score(prize+500000)
        print("\n#15. Something in an obvious location is said to be \"right under your\" what?")
        print("A. Mattress")
        print("B. Nose")
        print("C. Azaleas")
        print("D. Shorts")
        pick = input("\nWhat is your final answer? (A/B/C/D) \nAnswer: ").lower()
        if pick == "b":
            print("\nThat is correct!")
            win(prize,name)
            again(prize)
            stop = False
        if pick != "b":
            print("\nI'm sorry {}, that's the wrong answer.".format(name))
            lose(prize)

def show_score(prize):
    print("Your total prize money is now ${}!".format(prize))

def win(prize,name):
    print("\nCongratulations {}! You've won $1,000,000 today on Who Wants to Be A Millionaire! Incredible!".format(name))
    again(prize)

def lose(prize):
    print("\nYou've lost. Thank you for playing here today.")
    again(prize)

def again(prize):
    stop = True
    while stop:
        choice = input("\nWould you like to play again? (Y/N)\nAnswer: ").lower()
        if choice == "y":
            stop = False
            reset(prize,name)
        if choice == "n":
            print("\nThanks for playing. Come again!")
            stop = False
            quit()
        else:
            print("\nPlease enter 'Y' for 'Yes', or 'N' for 'No'")

def reset(prize,name):
    prize = 0
    start(prize,name)

if __name__ == "__main__":
    start()
