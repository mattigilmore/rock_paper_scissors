import random
run_loop=True
while  run_loop==True:
    #1==rock 2==paper 3==scissors
    computer=random.randint(1,3)
    print("pc pick:"+str(computer))
    pick_loop=True
    replay_loop=True
    replay=y
    while pick_loop==True:
        print("pick 1)rock 2)paper 3)scissors \n")
        player=input()
        print(type(player))
        if player=="1" or player=="2" or player=="3":
            player=int(player)
            if player==computer:
                print("It  is a tie would you like to play again y/n \n")
                repley=input()
                while replay_loop==True:
                        if replay==y:
                           pick_loop=False
                           break
                        else:
                            run_loop=pick_loop=False
                            break
            elif player==1:
                    if compture==2:
                        print("You LOSE;/( would you like to try again y/n \n")
                        while replay_loop==True:
                        repley=input()
                         if replay==y:
                            pick_loop=False
                            break
                         else:
                            run_loop=pick_loop=False
                            break
                    else:
                         print("You WIN!!!! would you like to try again y/n \n")
                        while replay_loop==True:
                        repley=input()
                         if replay==y:
                            pick_loop=False
                            break
                        else:
                            run_loop=pick_loop=False
                            break
         elif player==2:
                    if compture==3:
                        print("You LOSE;/( would you like to try again y/n \n")
                        while replay_loop==True:
                        repley=input()
                         if replay==y:
                            pick_loop=False
                            break
                        else:
                            run_loop=pick_loop=False
                            break
                    else:
                         print("You WIN!!!! would you like to try again y/n \n")
                        while replay_loop==True:
                        repley=input()
                         if replay==y:
                            pick_loop=False
                            break
                        else:
                            run_loop=pick_loop=False
                            break
         elif player==3:
                    if compture==1:
                        print("You LOSE;/( would you like to try again y/n \n")
                        while replay_loop==True:
                        repley=input()
                         if replay==y:
                            pick_loop=False
                            break
                        else:
                            run_loop=pick_loop=False
                            break
                    else:
                         print("You WIN!!!! would you like to try again y/n \n")
                         while replay_loop==True:
                         repley=input()
                         if replay!=y:
                            pick_loop=False
                            break
                        else:
                            run_loop=pick_loop=False
                            break




        else:
            print("please select valid choice \n")

print("thank you for playing")


