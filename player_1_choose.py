from pick_single_or_multi_player import pick_single_or_multi_player
from invalid_input import invalid_input
def player_1_choose():
    multi_choose = True
    while multi_choose == True:
        print("Player 1 turn \n")
        print("pick 1)rock 2)paper 3)scissors \n")
        computer = input()
        if computer == "1" or computer == "2" or computer == 3:
            print("player 2 turn \n")
            break
        else:
            print(invalid_input)