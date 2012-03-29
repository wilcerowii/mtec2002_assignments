import random
Name = raw_input ("Enter Name here: ") 
print "Hello " + Name + "this is a game test yout skills"
answer = raw_input ("Do you want to play? : ")
if answer == ("yes"):
    print "Okay! Lets play!"
    PC = raw_input ("Choose rock,paper or scissors: ")
    rand = random.randint(1, 3) #1 means rock,2 means paper,3 means scissors	  

    if PC == ("rock"):
        if rand == (1):
            print "Tie game!"
        elif rand == 2:
            print "Game lost!"
        elif rand == 3:
            print "Game Win!"
    if PC == ("paper"):
        if rand == 2:
            print "Tie game!"
        elif rand == 3:
            print "Game lost!"
        elif rand == 1:
            print "Game Win!"
    if PC == ("scissors"):
        if rand == 3:
            print "Tie game!"
        elif rand == 1:
            print "Game lost!"
        elif rand == 2:
            print "Game Win!"
else :
    print "aww!"
"""else (quit)



Rock, paper, scissors

    _______
---    ____)
      (_____)
      (_____)
      (____)
---.__(___)

    _______
---    ____)____
          ______)
          _______)
         _______)
---.__________)

    _______
---    ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


