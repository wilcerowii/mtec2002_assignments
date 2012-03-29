import random
print Rock"""
    _______
---    ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
print paper"""
    _______
---    ____)____
          ______)
          _______)
         _______)
---.__________)
"""
print scissors"""
    _______
---    ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



scores = {'player':0,'computer':0}
Name = raw_input ("Enter Name here: ") 
print "Hello " + Name + "this is a game test yout skills"
answer = raw_input ("Do you want to play? : ")
if answer == ("yes"):
    print "Okay! Lets play!"
    print "choose?"
    PC = raw_input ("Choose rock,paper or scissors: ")
    player = random.randint(1, 3) #1 means rock,2 means paper,3 means scissors	  

    if PC == ("rock"):
        if player== (1):
            print "Tie game!"
        elif player == 2:
            print "you lost!"
        elif player == 3:
            print "you Win!"
    if PC == ("paper"):
        if player == 2:
            print "Tie game!"
        elif player == 3:
            print "you lost!"
        elif player == 1:
            print "you Win!"
    if PC == ("scissors"):
        if player == 3:
            print "Tie game!"
        elif player == 1:
            print "yoou lost!"
        elif player == 2:
            print "you Win!"
    
elif command == "quit":
exit()




