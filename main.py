import random as rd

#ascii art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#player choice
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if choice ==0:
  print(f"You chose: 'Rock'\n {rock}")
elif choice==1:
  print(f"You chose: 'Paper'\n {paper}")
elif choice==2:
  print(f"You chose: 'Scissors'\n {scissors}")
else:
  print("invalid response")

#computer choice
computer_choice=rd.randint(0,2)
if computer_choice ==0:
  print(f"Computer chose: 'Rock'\n {rock}")
elif computer_choice==1:
  print(f"Computer chose: 'Paper'\n {paper}")
else:
  print(f"Computer chose: 'Scissors'\n {scissors}")

#winner announcement
if (choice==0 and computer_choice==0) or (choice==1 and computer_choice==1) or (choice==2 and computer_choice==2):
  print("It's a draw")
elif (choice==0 and computer_choice==1) or (choice==1 and computer_choice==2) or (choice==2 and computer_choice==0):
  print("Computer wins")
elif (choice==0 and computer_choice==2) or (choice==1 and computer_choice==0) or (choice==2 and computer_choice==1):
  print("You win")
