import constants
import math
import random
import sys
import pdb


teams_mod = []
players_mod =[]
exper_players = []
non_exper_players = []
num_exp_players_on_team = []
num_non_exp_players_on_team = []
all_guard_on_team = []
ex_team_1 = []
ex_team_2 = []
ex_team_3 = []
inex_team_1 = []
inex_team_2 = []
inex_team_3 = []
guardians_team_1 = []
guardians_team_2 = []
guardians_team_3 = []
height_ave_team_1 = []
height_ave_team_2 = []
height_ave_team_3 = []
run = 0
teams_mod.extend(constants.TEAMS)
players_mod.extend(constants.PLAYERS)
  
print("BASKETBALL TEAM STATS TOOL   ")
if __name__ == '__main__':
    while True:    
        def team_stats():
            team_num = 1
            print("\n""TEAMS")
            for team in teams_mod:
                num_teams = len(teams_mod)
                print("{}) {}".format(team_num, team[0:]))
                team_num += 1
                if team_num > len(teams_mod):
                    when_to_run_func()
                
        def when_to_run_func():
            global run
            run += 1
            if run == 1:
                clean_players()
                exp_players()
            team_sel()   
        
                    
        def team_sel():
            input_valid = False  # let's assume from the beginning that the input isn't valid
            while not input_valid:  # keep asking until we actually get valid input
                try:
                    team_selected = int(input("\n""To select which teams stats to view enter an option [1], [2], or [3]""\n" "> " ))
                    print(team_selected)
                except ValueError:
                    print("That was not a valid input. Please pick a number between [1] and [3]")
                else:    
                    if team_selected >= 4:
                        print("That was not a valid input. Please pick a number between [1] and [3] ")
                    elif team_selected <= 0:    
                        print("That was not a valid input. Please pick a number between [1] and [3] ")
                    else:
                        input_valid = True  # if it made it down here then the input was ok so set input_valid to True
                        team_name_sel = teams_mod[team_selected - 1]
                        print("\n""Team: {} Stats".format(team_name_sel))
                        print("--------------------")
                        players_per_team = len(players_mod) / len(teams_mod) 
                        print("Total Players: {}".format(int(players_per_team)))
                        if team_selected == 1:
                            team = ex_team_1
                        elif team_selected == 2:
                            team = ex_team_2
                        elif team_selected == 3:
                            team = ex_team_3
                        exp_play_name_qty(team, team_selected)  
                    
        def exp_play_name_qty(team_num, team_selected):
            if len(ex_team_1 or ex_team_2 or ex_team_3) == 0:
                num_exp_player_on_team = len(exper_players) / len(teams_mod)
            elif len(ex_team_1 or ex_team_2 or ex_team_3) != 0:
                num_exp_player_on_team = max(len(ex_team_1), len(ex_team_2), len(ex_team_3 ))    
                if len(team_num) == num_exp_player_on_team:
                    print("Experienced Players on Team QTY [{}]:""\n""{}" .format(int(num_exp_player_on_team),', '.join(team_num)))
                    if team_selected == 1:
                        in_team = inex_team_1
                    elif team_selected == 2:
                        in_team = inex_team_2
                    elif team_selected == 3:
                        in_team = inex_team_3
                    inexp_play_name_qty(in_team, team_selected, team_num)
            for exper_player in exper_players:
                names = exper_player['name']
                team_num.append(names)
                if len(team_num) == num_exp_player_on_team:
                    print("Experienced Players on Team QTY [{}]:""\n""{}" .format(int(num_exp_player_on_team),', '.join(team_num)))
                    if team_selected == 1:
                        in_team = inex_team_1
                    elif team_selected == 2:
                        in_team = inex_team_2
                    elif team_selected == 3:
                        in_team = inex_team_3
                    inexp_play_name_qty(in_team, team_selected, team_num)
    
                    
        def inexp_play_name_qty(in_team_num, team_selected, team_num):
            if len(inex_team_1 or inex_team_2 or inex_team_3) == 0:
                num_inexp_player_on_team = len(non_exper_players) / len(teams_mod)
            elif len(inex_team_1 or inex_team_2 or inex_team_3) != 0:
                num_inexp_player_on_team = max(len(inex_team_1), len(inex_team_2), len(inex_team_3 ))    
                if len(in_team_num) == num_inexp_player_on_team:
                    print("Inexperienced Players on Team QTY [{}]:""\n""{}" .format(int(num_inexp_player_on_team),', '.join(in_team_num)))
                    if team_selected == 1:
                        guard_on_team = guardians_team_1
                    elif team_selected == 2:
                        guard_on_team = guardians_team_2
                    elif team_selected == 3:
                        guard_on_team = guardians_team_3
                    player_guardians(team_num, in_team_num,team_selected, guard_on_team) 
            for inexper_player in non_exper_players:
                names = inexper_player['name']
                in_team_num.append(names)
                if len(in_team_num) == num_inexp_player_on_team:
                    print("Inexperienced Players on Team QTY [{}]:""\n""{}" .format(int(num_inexp_player_on_team),', '.join(in_team_num)))
                    if team_selected == 1:
                        guard_on_team = guardians_team_1
                    elif team_selected == 2:
                        guard_on_team = guardians_team_2
                    elif team_selected == 3:
                        guard_on_team = guardians_team_3
                    player_guardians(team_num, in_team_num,team_selected, guard_on_team) 
                    
        def player_guardians(team_num, in_team_num,team_selected, guard_on_team):
            if len(guard_on_team) > 1:
                for guardians in guard_on_team:
                    for key,value in guardians.items():
                        if 'guardians' == key:
                            all_guard_on_team.extend(value)
                print("\n""Guardians for all players on the team:" "\n""{}".format(','.join(all_guard_on_team)))
                if team_selected == 1:
                    team_height_ave = height_ave_team_1
                elif team_selected == 2:
                    team_height_ave = height_ave_team_2
                elif team_selected == 3:
                    team_height_ave = height_ave_team_3
                player_ave_heights(team_num, in_team_num, team_height_ave)
            for guardians in exper_players:
                for key,value in guardians.items():
                    if value in team_num:
                        guard_on_team.extend(exper_players[0:3])
                for guardians in non_exper_players:
                    for key,value in guardians.items():
                        if value in in_team_num:
                            guard_on_team.extend(non_exper_players[0:3])
                            for guardians in guard_on_team:
                                for key,value in guardians.items():
                                    if 'guardians' == key:
                                        all_guard_on_team.extend(value)
                            print("\n""Guardians for all players on the team:" "\n""{}".format(','.join(all_guard_on_team)))
                            if team_selected == 1:
                                team_height_ave = height_ave_team_1
                            elif team_selected == 2:
                                team_height_ave = height_ave_team_2
                            elif team_selected == 3:
                                team_height_ave = height_ave_team_3
                            player_ave_heights(team_num, in_team_num, team_height_ave)
                            
                            
                            
        def player_ave_heights(team_num, in_team_num, team_height_ave):
            players_per_team = len(players_mod) / len(teams_mod)
            all_ave_heights_sum = 0
            if len(team_height_ave) > 1:
                for heights in team_height_ave:
                    for key,value in heights.items():
                        if 'height' == key:
                            all_ave_heights_sum += value
                print("\n""Average height for all players on the team: {}".format(int(all_ave_heights_sum / players_per_team)))
                clear_used_players(team_num, in_team_num)  
            for heights in exper_players:
                for key,value in heights.items():
                    if value in team_num:
                        team_height_ave.extend(exper_players[0:3])
                for heights in non_exper_players:
                    for key,value in heights.items():
                        if value in in_team_num:
                            team_height_ave.extend(non_exper_players[0:3])
                            for heights in team_height_ave:
                                for key,value in heights.items():
                                    if 'height' == key:
                                        all_ave_heights_sum += value
                            print("\n""Average height for all players on the team: {}".format(int(all_ave_heights_sum / players_per_team)))
                            clear_used_players(team_num, in_team_num)
            
                    
        def clear_used_players(team_num, in_team_num):
            del all_guard_on_team[:]
            for names in exper_players:
                for key,value in names.items():
                    if value in team_num:
                        del exper_players[0:3]
            for in_names in non_exper_players:
                for key,value in in_names.items():
                    if value in in_team_num:
                        del non_exper_players[0:3]            
                        main_menu()
        
        
        def clean_players():
            for heights in players_mod:      
                for k,v in heights.items():    
                    if 'height' in k:   
                        heights[k] = (v).split(' ')     
            for heights in players_mod:
                for k,v in heights.items():       
                    if 'height' in k:   
                        heights[k] = int(v[0])    
            for experience in players_mod:
                for k,v in experience.items():
                    if 'experience' in k :
                        if v != 'YES':
                            experience[k] = False
                        elif v == 'YES':
                            experience[k] = True
            for guardians in players_mod:      
                for k,v in guardians.items():    
                    if 'guardians' in k:   
                        guardians[k] = (v).split('and') 
                        
        
        def exp_players():
            for experience in players_mod:
                for k,v in experience.items():
                    if 'experience' in k:
                        if v == True:
                            exper_players.append(experience)
                        elif v == False:
                            non_exper_players.append(experience)
            random.shuffle(exper_players)
            random.shuffle(non_exper_players)
    
        
        def exit_stats():
            print("\n""Thank you for using the BASKETBALL TEAM STATS TOOL, see y'all next time.""\n")
            sys.exit()
            
        
        def main_menu():
            print("\n""---- MENU -----""\n")
            print("Would you like to Display Team Stats or Exit""\n""1) Display Team Stats""\n""2) Exit""\n")
            try:
                menu_option = int(input("Enter an option [1] or [2] > "))
            except ValueError:  
                print("That was not a valid input. Please pick a number between [1] and [2]")
            else:        
                if menu_option == 1:
                    team_stats()
                elif menu_option == 2:
                    exit_stats()
                elif menu_option != 1 or 2:
                    print("That was not a valid input. Please pick a number between [1] and [2")
            
        main_menu()        
            
    
    
    



    