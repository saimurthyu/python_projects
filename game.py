import random

while True:
   choice=["rock","paper","scissors"]
   computer=random.choice(choice)
   player=None

   while player not in choice:
      player=input("Enter rock,paper,or scissors: ").lower()

      if player==computer:
       print("computer: ",computer)
       print("player: ",player)
       print("Tie!")
      elif player=="rock":
       if computer=="paper":
           print("computer: ",computer)
           print("player: ",player)
           print("You Lose :(") 
      elif player=="rock":
         if computer=="scissors":
              print("computer: ",computer)
              print("player: ",player)
              print("You won :)")      
      elif player=="paper":
        if computer =="rock":
             print("computer: ",computer)
             print("player: ",player)
             print("You won :)")
      elif player=="paper":
         if computer=="scissors": 
             print("computer: ",computer)
             print("player: ",player)
             print("You Lose :(")     
      elif player=="scissors":
        if computer=="paper":
             print("computer: ",computer)
             print("player: ",player)
             print("You won :)")
      elif player=="scissors":
         if computer=="rock":
             print("computer: ",computer)
             print("player: ",player)
             print("You Lose :(")

   play_again=input("play again? (yes/no): ").lower()

   if play_again !="yes":
       break
print("bye  :( see you again")   

          



    