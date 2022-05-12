import time
#the website to try this is https://codehs.com/sandbox/id/html-ln3Gl4
def startgame3(): 
    if startgamefloat == 192011820:
        level0()
    elif startgamefloat != 192011820:
        print("Hint: The password is start.")
        print("Hint: It's a numbers to letters code.")
        print("One More Chance!")
        stargamefloatryagain()
    else:
        print("Game Over. Try Again?")
#ansers are 4, 6.5, 32.65,88, 687, 3786.54
Name = input("Please enter your name here: ")
def end1():
    for i in range(10):
        time.sleep(0.5)
        print("The Cake is a lie", Name)
    endgame = input("Type 'Stop' (No Spaces) in numbers to end the game! ")
    endgame1 = float(endgame)
    if endgame1 == 19201516:
        print("Good Game")
    else:
        print("Try Again!")
        time.sleep(1)
        startgame3()
def stargamefloatryagain():
    startgame1 = input("Enter The Correct Code to Start the Game! ")
    startgamefloat1 = float(startgame1)
    if startgamefloat1 == 192011820:
        level0()
    else:
        print("Game over. Try Again?")
def level0():
    var = input("Level one: Give us a number between zero and 10! ")
    var1 = float(var)
    if var1 == 4:
        print("You Win! On to the next level.")
        levelone()
    else:
        print("Game Over... Try again??")
def lastlevel():
    lastlevel = input("Last Level! You got this! Please input a number between 0 and 5000! ")
    lastlevelfloat = float(lastlevel)
    if lastlevelfloat == 3786.54:
        print("WOW! YOU DID IT! WAIT A FEW SECONDS FOR THE GRAND PRIZE!!!")
        time.sleep(2)
        end1()
    else:
        print("NOOOOOO!!! YOU WERE SO CLOSE!!! Try Again?")
def levelfourintto1000():
    levelfour1000 = input("How are you on level five??? Anyways, please input a number between 0 and 1000! ")
    levelfour1000float = float(levelfour1000)
    if levelfour1000float == 687:
        print("WHATTTTTTTT????? You Got It right???? Anyways, on to your last level before the grand prize!")
        lastlevel()
    else:
        print("Game Over :( ")
def levelthreeintto100():
    levelthree = input("Level four! give me a number between 1 and 100! ")
    floatlevelthree = float(levelthree)
    if floatlevelthree == 88:
        print("You Looked at the source code, didn't you! If you did not, On to the next level!")
        levelfourintto1000()
    else:
        print("Game over. You were so close, keep trying!")
def leveltwofloatstofifty():
    leveltwo50 = input("Level three! Give us a number between 1 and 50! ")
    leveltwo50float = float(leveltwo50)
    if leveltwo50float == 32.65:
        print("Wow! Your really good at this! On to the next level!")
        levelthreeintto100()
    else:
        print("Good Try! Try Again?")
def levelone():
    level1 = input("Level two! Give us a number between 1 and 20! ")
    level1float = float(level1)
    if level1float == 6.5:
        print("Good job! On to the next level!")
        print(leveltwofloatstofifty())
    else:
        print("You lose.")
        print("hint: (this number has a decimal point!)")
#startnum is 192011820
startgame = input("Enter The Correct Code to Start the Game! ")
startgamefloat = float(startgame)
if startgamefloat == 666:
    end1()
else:
    startgame3()
