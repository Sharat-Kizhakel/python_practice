import random
from pyfiglet import figlet_format
# import pywhatkit as pwt

moves = ['Rock', 'Paper', 'Scissor']
user_score = 0
opp_score = 0
# pwt.image_to_ascii_art(
#     "C:\\Users\\admin\\Desktop\\rock_paper_scissor_img.png", "C:\\Users\\admin\\Desktop\\rock_paper_scissor_img.txt")
# path = "C:\\Users\\admin\\Desktop\\rock_paper_scissor_img.txt"
# with open(path) as f:
#     lines = f.readlines()
# f.close()
# print(lines)


def winning_move(choice):
    outcome = ""
    global user_score
    global opp_score
    opp_choice = moves.index(random.choice(moves))+1
    if choice == opp_choice:
        outcome = "DRAW"
        user_score += 0
        opp_score += 0
    elif (choice == 1 and opp_choice == 2):
        outcome = "LOST"
        user_score += 0
        opp_score += 1
    elif (choice == 1 and opp_choice == 3):
        outcome = "WON"
        user_score += 1
        opp_score += 0
    elif (choice == 2 and opp_choice == 3):
        outcome = "LOST"
        user_score += 0
        opp_score += 1
    elif(choice == 2 and opp_choice == 1):
        outcome = "WON"
        user_score += 1
        opp_score += 0
    elif(choice == 3 and opp_choice == 2):
        outcome = "WON"
        user_score += 1
        opp_score += 0
    elif(choice == 3 and opp_choice == 1):
        outcome = "LOST"
        user_score += 0
        opp_score += 1
    return outcome, user_score, opp_score


def init_score():
    global user_score
    user_score = 0
    global opp_score
    opp_score = 0


global user_continue
user_continue = True
while user_continue == True:

    count = 0
    init_score()  # re-initializing the scores
    no_of_rounds = int(input('Enter the number of rounds:\n'))
    while count != no_of_rounds:

        user_choice = int(
            input("Please select your move:\n1.Rock\n2.Paper\n3.Scissor\n"))
        if user_choice == 1:
            result, u_score, o_score = winning_move(user_choice)
            print("RESULT OF ROUND "+str(count+1)+":"+result+"\n"+"user score:" +
                  str(u_score)+"\n"+"opp score:"+str(o_score))
        elif user_choice == 2:
            result, u_score, o_score = winning_move(user_choice)
            print("RESULT OF ROUND "+str(count+1)+":"+result+"\n"+"user score:" +
                  str(u_score)+"\n"+"opp score:"+str(o_score))
        elif user_choice == 3:
            result, u_score, o_score = winning_move(user_choice)
            print("RESULT OF ROUND "+str(count+1)+":"+result+"\n"+"user score:" +
                  str(u_score)+"\n"+"opponent score:"+str(o_score))
        count += 1
    winner = "user" if user_score > opp_score else "opponent"
    print(figlet_format("CONGRATULATIONS {} YOU WON".format(
        winner), font="cybermedium"))
    print("\n")
    print(figlet_format("SCORE:{}".format(user_score), font="standard")) if winner is "user" else print(
        (figlet_format("SCORE:{}".format(str(opp_score)), font="standard")))
    print("\n")
    user_continue = input("DO YOU WANT TO PLAY AGAIN?:y/n\n")

    user_continue = True if user_continue is "y" else quit()
