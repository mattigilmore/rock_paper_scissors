import random
loop1=True
player=None
compture=None
game=True
pick_loop=True
win=0
lose=0
tie=0
pc_or_multi="m"
def invalid_input():
     return print("please select valid choice \n")
while game==True:
    print("would you like to play again 1) compputer or 2) another player")
    pc_or_multi= input()
    if pc_or_multi =="1" or  pc_or_multi=="2":
        break
    else:
        invalid_input()
while game==True:

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
        if player=="1" or player=="2" or player=="3":
            if player==computer:
                tie=tie+1
                print("It's a Tie\n")
                break
            elif player=="1":
                if computer=="2":
                    lose=lose+1
                    print("You Lose \n")
                    break
                else:
                    win=win+1
                    print("you Win ! \n")
                    break
            elif player =="2":
                if computer=="3":
                    lose= lose+1
                    print("you lose \n")
                    break
                else:
                    win=win+1
                    print("You Win ! \n")
            else:
                if computer=="1":
                    lose=lose+1
                    print("you lose \n")
                    break
                else:
                    win=win+1
                    print("You Win !\n")
                    break

        else:
            invalid_input()
    print("Wins :"+str(win)+" Loses:"+str(lose)+" Ties:"+str(tie)+"\n")
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