from invalid_input import invalid_input
from pick_single_or_multi_player import pick_single_or_multi_player



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
computer=None

while  run_loop==True:
    #1==rock 2==paper 3==scissors

    #print("pc pick:"+str(computer))
    pick_loop=True
    replay_loop=True
    played=False #added this to hopefully fix line 99 from bugging
    replay="y"
    while pc_multi==True:
        pick_single_or_multi_player()

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
                                   print("loop true")
                                   break
                               else:

                                    print("loop false")
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
                invalid_input()

print("thank you for playing")

