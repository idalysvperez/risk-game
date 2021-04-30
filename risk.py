#Risk_Die_Game_Mini_Project
#Idalys_Perez
#DS4A

import numpy as np
def play_risk_game():
    print('Welcome to the Risk Dice Game')
    begin_game = input('Click s to start game')
    if begin_game == 's':
        a_units = int(float(input('Number of attacking units:')))
        d_units = int(float(input('Number of defending units:')))
        end_attack = int(float(input('End attacking when attacking units reaches:')))
        round_number = 0
        while (a_units > end_attack):
            attacker_roll = []
            defender_roll = []
            a_limit = 0
            d_limit = 0
            round_number += 1
            print("-------------------")
            print("Round:")
            print(round_number)
            print("-------------------")
            if (a_units > 2):
                a_limit = 3
            else: 
                a_limit = a_units
            if (d_units > 1):
                d_limit = 2
            else: 
                d_limit = 1
            for i in range(a_limit):
                print('The attacker rolled:')
                x = np.random.randint(1,6)
                attacker_roll.append(x)
                print(attacker_roll[-1])
            for j in range(d_limit):
                print('The defender rolled:')
                y = np.random.randint(1,6)
                defender_roll.append(y)
                print(defender_roll[-1])
            attacker_roll.sort(reverse = True)
            defender_roll.sort(reverse = True)
            dice_comparison = zip(attacker_roll, defender_roll)
            for pair in dice_comparison: 
                attacker, defender = pair 
                if attacker > defender: 
                    d_units -= 1
                else: 
                    a_units -= 1
            if (a_units == end_attack) or (d_units == 0):
                break
    print("-------------------")
    print('Attackers remaining:')
    print(a_units)
    print('Defenders remaining:')
    print(d_units)
    print("-------------------")
    if d_units > 0: 
        print('Defenders win the game')
    else: 
        print('Attackers win the game')
        
        
play_risk_game()