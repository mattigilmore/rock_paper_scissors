

import random

from pyasn1.compat.octets import null
win1=0
lose1=0
tie1=0
win2=0
lose2=0
tie2=0
end_game=False
pc_or_multi="0"
pc_multi=True
run_loop=True
invalid_input="please select valid choice \n"
while  run_loop==True:
    #1==rock 2==paper 3==scissors

    #print("pc pick:"+str(computer))
    pick_loop=True
    replay_loop=True
    played=False #added this to hopefully fix line 99 from bugging
    replay="y"
    while pc_multi==True:
        if pc_or_multi=="0":
            print("play againest 1)computer or 2)another person")
            pc_or_multi=input()
        else:
            pass
        while pc_or_multi=="1" or pc_or_multi=="2":
            if pc_or_multi=="1":
                computer = random.randint(1, 3)
                break
            elif pc_or_multi =="2":
                multi_choose=True
                while multi_choose==True:
                    print("Player 1 turn \n")
                    print("pick 1)rock 2)paper 3)scissors \n")
                    computer = input()
                    if computer=="1" or computer=="2" or computer==3:
                        print("player 2 turn \n")
                        break
                    else:
                        pick_loop=False
                        print(invalid_input)
        while pick_loop==True:
            print("pick 1)rock 2)paper 3)scissors \n")
            player=input()

            if player=="1" or player=="2" or player=="3":
                player=int(player)
                played=True
                if player==computer:
                    if pc_or_multi=="2":
                        print("It  is a tie would you like to play again y/n \n")
                        tie2+=1
                        tie1+=1
                    else:
                        tie2+=1
                        print("It  is a tie would you like to play again y/n \n")
                        replay=input()

                    while replay_loop==True:
                            if replay=="y":

                               break
                            else:
                                end_game=True
                                run_loop=pick_loop=False
                                break
                elif player==1:
                        if computer==2:
                            lose2+=1
                            if pc_or_multi=="2":
                                win1+=1
                                print("player 1 wins \n Would you like to play again \n")
                            else:
                                print("you LOSE;(  would you like to try again y/n \n")
                            while replay_loop==True:
                               replay=input()
                               if replay=="y":

                                 break
                               else:
                                 end_game=True
                                 run_loop=pick_loop=False
                                 break
                        else:
                            win2+=1
                            if pc_or_multi=="2":
                                lose1+=1
                                print("player 2 Wins \n Would you like to play again \n")
                            else:
                                print("you WIN!!!! would you like to try again y/n \n")

                            while replay_loop==True:
                                replay=input()
                                if replay=="y":

                                  break
                                else:
                                  end_game=True
                                  run_loop=pick_loop=False
                                  break
                elif player==2:
                     if computer==3:
                         lose2+=1
                         if pc_or_multi=="2":
                             win1+=1
                             print("player 1 wins \n would you like to play again\n")
                         else:
                             print("you LOSE;(  would you like to try again y/n \n")
                         while replay_loop==True:
                            replay=input()

                            if replay=="y":

                                break
                            else:
                                end_game=True
                                run_loop=pick_loop=False
                                break
                     else:
                         win2+=1
                         print("you WIN!!!! would you like to try again y/n \n")

                         while replay_loop==True:
                             replay=input()
                             if replay=="y":

                                break
                             else:
                                end_game=True
                                run_loop=pick_loop=False
                                break

                else:
                    win2+=1
                    if pc_or_multi=="2":
                        lose1=+1
                        print("player 2 wins \n would you like to play again \n")
                    else:
                        print("you WIN!!!! would you like to try again y/n \n")

                    while replay_loop==True:
                        replay=input()
                        if replay!="y":

                            break
                        else:
                            end_game=True
                            run_loop=pick_loop=False
                            break

                print("player 1\n")
                print("wins:" + str(win1) + "  lose:" + str(lose1) + " ties:" + str(tie1) + "\n")
                print("player 2\n")
                print("wins:" + str(win2) + "  lose:" + str(lose2) + " ties:" + str(tie2) + "\n")
                if end_game==True:
                    break
                else:
                    pass
            elif end_game==True:
                break
            else:
                print(invalid_input)

print("thank you for playing")

