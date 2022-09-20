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

# #player choice
# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
# if choice ==0:
#   print(f"You chose: 'Rock'\n {rock}")
# elif choice==1:
#   print(f"You chose: 'Paper'\n {paper}")
# elif choice==2:
#   print(f"You chose: 'Scissors'\n {scissors}")
# else:
#   print("invalid response")
# 
# #computer choice
# computer_choice=rd.randint(0,2)
# if computer_choice ==0:
#   print(f"Computer chose: 'Rock'\n {rock}")
# elif computer_choice==1:
#   print(f"Computer chose: 'Paper'\n {paper}")
# else:
#   print(f"Computer chose: 'Scissors'\n {scissors}")
# 
# #winner announcement
# if (choice==0 and computer_choice==0) or (choice==1 and computer_choice==1) or (choice==2 and computer_choice==2):
#   print("It's a draw")
# elif (choice==0 and computer_choice==1) or (choice==1 and computer_choice==2) or (choice==2 and computer_choice==0):
#   print("Computer wins")
# elif (choice==0 and computer_choice==2) or (choice==1 and computer_choice==0) or (choice==2 and computer_choice==1):
#   print("You win")

#Version 2.1. Added recurssion when the result is a draw. Reduced if-else statements. Added lists and dict to structure data.

art = [rock, paper, scissors]
choice_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}

#players choices
def player_hand():
    choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
    player_chose = choice_dict[choice]
    print(art[choice])
    return player_chose

#computers random choices
def computer_hand():
    random_gen = random.randint(0, 2)
    computer_chose = choice_dict[random_gen]
    print(art[random_gen])
    return computer_chose

#Winner announcement
def result(player, computer):
    # 0 : player wins, 1: computer wins
    if (player == "Rock" and computer == "Paper") or (player == "Scissors" and computer == "Paper") or (player == "Rock" and computer == "Scissors"):
        print("You win")
    elif (player == "Paper" and computer == "Rock") or (player == "Paper" and computer == "Scissors") or (player == "Scissors" and computer == "Rock"):
        print("Computer wins")
    else:
        print("Draw")
        game()
        
#game body
def game():
    player_choice = player_hand()
    print(f"You chose: {player_choice}")
    computer_choice = computer_hand()
    print(f"Computer chose: {computer_choice}")
    result(player_choice, computer_choice)

game()
