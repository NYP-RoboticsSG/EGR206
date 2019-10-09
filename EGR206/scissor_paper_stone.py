import random

choice = ['scissors','paper','stone']
rand_choice = random.choice(choice)

while True:
    print("Let play scissors paper stone")
    print("Please enter scissors, paper or stone")
    user_choice = input("Enter your choice: ")
    while not(user_choice.lower() in choice):
        print("Sorry wrong input plase enter again\n")
        user_choice = input("Enter your choice: ")

    print("You choose",user_choice,"my choice is", rand_choice)
    if user_choice.lower() == "stone" and rand_choice == "scissors":
        print("Congratualation you win")
    elif user_choice.lower() == "paper" and rand_choice == "stone":
        print("Congratualation you win")
    elif  user_choice.lower() == "scissors" and rand_choice == "stone":
        print("Congratualation you win")
    elif user_choice.lower() == rand_choice :
        print("Its a draw")
    else:
        print("Sorry.. Computer win... Lets try again..")
    print("\n")
