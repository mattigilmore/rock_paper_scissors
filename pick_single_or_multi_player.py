import random
from player_1_choose import * 
pc_or_multi="0"
def pick_single_or_multi_player():
    if pc_or_multi !="0" or "1" or "2":
        pc_or_multi="0"
    else:
        pass

    if pc_or_multi == "0":
        print("play againest 1)computer or 2)another person")
        pc_or_multi = input()
    else:
        pass
    while pc_or_multi == "1" or pc_or_multi == "2":
        if pc_or_multi == "1":
            computer = random.randint(1, 3)
            break
        elif pc_or_multi == "2":
            player_1_choose()
pick_single_or_multi_player()
