# list of questions
import random
global questions
questions = [
    {"Grand Central Terminal, Park Avenue, New York is the world's":
     [
         "A.largest railway station",
         "B.highest railway station",
         "C.longest railway station",
         "D.None of the above"
     ]},
    {'Entomology is the science that studies':

     ["A.Behavior of human beings",
      "B.Insects",
      "C.The origin and history of technical and scientific terms",
      "D.The formation of rocks"]},
    {'Eritrea, which became the 182nd member of the UN in 1993, is in the continent of':

     ["A.Asia",
      "B.Africa",
      "C.Europe",
      "D.Australia"]},
    {'For which of the following disciplines is Nobel Prize awarded?':

     ['A.Physics and Chemistry',
      'B.Physiology or Medicine',
      'C.Literature, Peace and Economics',
      'D.All of the above']
     }]

answers = [{"Grand Central Terminal, Park Avenue, New York is the world's": 'A'}, {"Entomology is the science that studies": 'B'}, {
    'Eritrea, which became the 182nd member of the UN in 1993, is in the continent of': 'B'}, {'For which of the following disciplines is Nobel Prize awarded?': 'D'}]


def check_answer(user_input, key):
    for block in answers:

        if key == (' '.join(list(block.keys()))):

            if (' '.join(list(block.values()))) == user_input:
                return True
            else:
                return False


def play_again():
    continue_game = input("Do you want to play again y/n?:\n")
    return continue_game


def new_game():
    c = 0
    user_score = 0
    global game
    game = True
    while game:

        while(c != 4):
            ques = random.choice(questions)
            quest = ' '.join(list(ques.keys()))
            print(50*"-")
            print(quest+":"+"\n")
            for option in ques.values():
                ans_option = '\n'.join(list(option))
                print(ans_option)

            user_input = input("Enter option: \nA.\nB.\nC.\nD.\n")
            is_correct = check_answer(user_input, quest)
            if is_correct:
                user_score += 1
                print("CORRECT ANS, SCORE IS:{}".format(user_score))
            else:
                user_score += 0
                print("WRONG ANS, SCORE IS:{}".format(user_score))
            c += 1
        choice = play_again()
        new_game() if choice == 'y' else quit()


new_game()
