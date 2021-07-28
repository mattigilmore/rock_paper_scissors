import random
loop1=True
player=None
compture=None
game=True
pick_loop=True
def invalid_input():
     return print("please select valid choice \n")
while game==True:
    global pc_or_multi

    print("would you like to play again 1) compputer or 2) another player")
    pc_or_multi= input()
    if pc_or_multi =="1" or  pc_or_multi=="2":
        pass
    else:
        invalid_input()
    if pc_or_multi=="1":
        computer = random.randint(1, 3)
    else:
        while loop1==True:

            print("Player 1 turn \n")
            print("pick 1)rock 2)paper 3)scissors \n")
            computer = input()
            if computer == "1" or computer == "2" or computer == 3:
                print("player 2 turn \n")
                multi_choose = False
                break
            else:
                print(invalid_input)
    while pick_loop == True:
        print("pick 1)rock 2)paper 3)scissors \n")
        player = input()
        if player=="1" or "2" or "3":
            break
        else:
            invalid_input()
    while pick_loop==True:
        print("would you like to play again? y/n \n")
        play_again=input()
        if play_again=="y" or play_again=="n":
            if play_again=="y":
                break
            else:
                game=False
                break
        else:
            invalid_input()
print(player)