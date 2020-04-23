"""Basketball Team Stats Tool"""
import constants
import copy
import math
import random
import sys



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
players_mod.extend(copy.deepcopy(constants.PLAYERS))  
print("BASKETBALL TEAM STATS TOOL   ")

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
        """The when_to_run_func only runs the clean_players() and exp_players()                 functions once. The program is modifying the lists these funcitons populate with         each loop and it wouldn't work if the lists were being repopulated.  
        """   
        global run
        run += 1
        if run == 1:
            clean_players()
            exp_players()
        team_sel()   
            
    if __name__ == '__main__':        
                    
        def team_sel():
            """While statement to get team selection from user with exception       handling"""
            input_valid = False  
            while not input_valid:  
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
                        input_valid = True 
                        """Need to increment user selected team_name_sel to match list index which starts from                         0 and not  1
                        """
                        team_name_sel = teams_mod[team_selected - 1]
                        print("\n""Team: {} Stats".format(team_name_sel))
                        print("--------------------")
                        players_per_team = len(players_mod) / len(teams_mod) 
                        print("Total Players: {}".format(int(players_per_team)))
                        """The if statments use the selected team to tell the program which list to store the                         experienced players in  the team chosen by user in the exp_play_name_qty() function
                        """
                        if team_selected == 1:
                            team = ex_team_1
                        elif team_selected == 2:
                            team = ex_team_2
                        elif team_selected == 3:
                            team = ex_team_3
                        exp_play_name_qty(team, team_selected)  
                        
    if __name__ == '__main__':                       
                    
        def exp_play_name_qty(team_num, team_selected):
            """If none of the expereinced players have been assigned to a team yet claculate the # of                     expereinced players for each team by dividing all the expereinced players available by the number             of teams to fill
            """
            if len(ex_team_1 or ex_team_2 or ex_team_3) == 0:
                num_exp_player_on_team = len(exper_players) / len(teams_mod)
                """If the list for one of the teams has already been populated during a previous loop then use           the # of players as the # of players for the rest of the teams
                """
            elif len(ex_team_1 or ex_team_2 or ex_team_3) != 0:
                num_exp_player_on_team = max(len(ex_team_1), len(ex_team_2), len(ex_team_3 )) 
                """ If the # of players on the team equals the # of players that should be on the team then                   print the out the players
                """
                if len(team_num) == num_exp_player_on_team:
                    print("Experienced Players on Team QTY [{}]:""\n""{}" .format(int(num_exp_player_on_team),', '.join(team_num)))
                    """The if statments use the selected team to tell the program which list to store the                         inexperienced players in  the team chosen by user in the exp_play_name_qty() function
                    """            
                    if team_selected == 1:
                        in_team = inex_team_1
                    elif team_selected == 2:
                        in_team = inex_team_2
                    elif team_selected == 3:
                        in_team = inex_team_3
                    inexp_play_name_qty(in_team, team_selected, team_num)
                    """if the team selected has not had experienced players assigned to the team then assign                       players to the team in the previously selected list
                    """
            for exper_player in exper_players:
                names = exper_player['name']
                team_num.append(names)
                if len(team_num) == num_exp_player_on_team:
                    print("Experienced Players on Team QTY [{}]:""\n""{}" .format(int(num_exp_player_on_team),', '.join(team_num)))
                    """The if statments use the selected team to tell the program which list to store the                         inexperienced players in  the team chosen by user in the exp_play_name_qty() function
                    """
                    if team_selected == 1:
                        in_team = inex_team_1
                    elif team_selected == 2:
                        in_team = inex_team_2
                    elif team_selected == 3:
                        in_team = inex_team_3
                    inexp_play_name_qty(in_team, team_selected, team_num)
    
                    
        def inexp_play_name_qty(in_team_num, team_selected, team_num):
            """If none of the in expereinced players have been assigned to a team yet claculate the # of                   inexpereinced players for each team by dividing all the inexpereinced players available by the               number of teams to fill
            """
            if len(inex_team_1 or inex_team_2 or inex_team_3) == 0:
                num_inexp_player_on_team = len(non_exper_players) / len(teams_mod)
                """If the list for one of the teams has already been populated during a previous loop then use                 the # of players as the # of players for the rest of the teams
                """
            elif len(inex_team_1 or inex_team_2 or inex_team_3) != 0:
                num_inexp_player_on_team = max(len(inex_team_1), len(inex_team_2), len(inex_team_3 ))  
                """ If the # of players on the team equals the # of players that should be on the team then                   print the out the players
                """
                if len(in_team_num) == num_inexp_player_on_team:
                    print("Inexperienced Players on Team QTY [{}]:""\n""{}" .format(int(num_inexp_player_on_team),', '.join(in_team_num)))
                    """The if statments use the selected team to tell the program which list to store the                         guardians for players in  the team chosen by user in the player_guardians() function
                    """                    
                    if team_selected == 1:
                        guard_on_team = guardians_team_1
                    elif team_selected == 2:
                        guard_on_team = guardians_team_2
                    elif team_selected == 3:
                        guard_on_team = guardians_team_3
                    player_guardians(team_num, in_team_num,team_selected, guard_on_team) 
                    """if the team selected has not had experienced players assigned to the team then assign                      players to the team in the previously selected list
                    """
            for inexper_player in non_exper_players:
                names = inexper_player['name']
                in_team_num.append(names)
                if len(in_team_num) == num_inexp_player_on_team:
                    print("Inexperienced Players on Team QTY [{}]:""\n""{}" .format(int(num_inexp_player_on_team),', '.join(in_team_num)))
                    """The if statments use the selected team to tell the program which list to store the                         guardians for players in  the team chosen by user in the player_guardians() function
                    """
                    if team_selected == 1:
                        guard_on_team = guardians_team_1
                    elif team_selected == 2:
                        guard_on_team = guardians_team_2
                    elif team_selected == 3:
                        guard_on_team = guardians_team_3
                    player_guardians(team_num, in_team_num,team_selected, guard_on_team) 
                    
        def player_guardians(team_num, in_team_num,team_selected, guard_on_team):
            """ If the List assigned to team selected already has a guardian then print out the list of                   Guardians on the team, if there are guardians on the list this team has already been selected                 don't repeat the selection
            """
            if len(guard_on_team) > 1:
                for guardians in guard_on_team:
                    for key,value in guardians.items():
                        if 'guardians' == key:
                            all_guard_on_team.extend(value)
                print("\n""Guardians for all players on the team:" "\n""{}".format(','.join(all_guard_on_team)))
                """The if statments use the selected team to tell the program which list to store the heights                 for players in  the team chosen by user in the player_ave_heights() function
                """
                if team_selected == 1:
                    team_height_ave = height_ave_team_1
                elif team_selected == 2:
                    team_height_ave = height_ave_team_2
                elif team_selected == 3:
                    team_height_ave = height_ave_team_3
                player_ave_heights(team_num, in_team_num, team_height_ave)
                """ For team selected and use the experienced players selected to select the guardians for                     experinced players on the team and place the guardian information in a list assigned to team                 chosen.
                """
            for guardians in exper_players:
                for key,value in guardians.items():
                    if value in team_num:
                        guard_on_team.extend(exper_players[0:3])
                        """ For team selected and use the inexperienced players selected to select the                                 guardians for inexperinced players on the team and place the guardian information in                         a list assigned to team chosen.
                        """                        
                for guardians in non_exper_players:
                    for key,value in guardians.items():
                        if value in in_team_num:
                            guard_on_team.extend(non_exper_players[0:3])
                            """ Creates a list with only the guardian names from both exerienced and                                       inexpereinced players
                            """
                            for guardians in guard_on_team:
                                for key,value in guardians.items():
                                    if 'guardians' == key:
                                        all_guard_on_team.extend(value)
                            print("\n""Guardians for all players on the team:" "\n""{}".format(','.join(all_guard_on_team)))
                            """The if statments use the selected team to tell the program which list to store                             the heights for players in  the team chosen by user in the player_ave_heights()                               function
                            """
                            if team_selected == 1:
                                team_height_ave = height_ave_team_1
                            elif team_selected == 2:
                                team_height_ave = height_ave_team_2
                            elif team_selected == 3:
                                team_height_ave = height_ave_team_3
                            player_ave_heights(team_num, in_team_num, team_height_ave)
                            
                            
                            
        def player_ave_heights(team_num, in_team_num, team_height_ave):
            """Calculates players per team by dividing all the players by the number of teams"""
            players_per_team = len(players_mod) / len(teams_mod)
            """Sets a running sum of all player heights to 0"""
            all_ave_heights_sum = 0
            """checkss to make sure that this is the first loop if it this is the 2nd loop heights have already been collected and stored so skip to print stayment
"""
            if len(team_height_ave) > 1:
                """ for 2nd request and their after to see a tems stats Loop through list for of teams                         specific height and pull out heights to be printed
                """
                for heights in team_height_ave:
                    for key,value in heights.items():
                        if 'height' == key:
                            all_ave_heights_sum += value
                print("\n""Average height for all players on the team: {}".format(int(all_ave_heights_sum / players_per_team)))
                clear_used_players(team_num, in_team_num) 
                """ Looping through experience players list and pulling out data for the players on the team                   selcted by user
                """
            for heights in exper_players:
                for key,value in heights.items():
                    if value in team_num:
                        team_height_ave.extend(exper_players[0:3])
                        """ Looping through inexperience players list and pulling out data for the players on                         the team selcted by user
                        """
                for heights in non_exper_players:
                    for key,value in heights.items():
                        if value in in_team_num:
                            team_height_ave.extend(non_exper_players[0:3])
                            """looping through players on selected team and pulling out the height information                             to get ready to print"""
                            for heights in team_height_ave:
                                for key,value in heights.items():
                                    if 'height' == key:
                                        all_ave_heights_sum += value
                            print("\n""Average height for all players on the team: {}".format(int(all_ave_heights_sum / players_per_team)))
                            clear_used_players(team_num, in_team_num)
            
                    
        def clear_used_players(team_num, in_team_num):
            """clears all the players that were selected from a team from the total pool of possible player
            """
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
            """Converts the height key value pair in players_mod dictionary value into an int"""
            for heights in players_mod:      
                for k,v in heights.items():    
                    if 'height' in k:   
                        heights[k] = (v).split(' ')     
            for heights in players_mod:
                for k,v in heights.items():       
                    if 'height' in k:   
                        heights[k] = int(v[0])  
                        """Converts the player experince value into a True or False Bool in the players_mod                           dictionary
                        """
            for experience in players_mod:
                for k,v in experience.items():
                    if 'experience' in k :
                        if v != 'YES':
                            experience[k] = False
                        elif v == 'YES':
                            experience[k] = True
                            """Removes the and from between guardians for players that have more then one                                 gaurdian for values in the Key=guardians in players_mod dictionary
                            """
            for guardians in players_mod:      
                for k,v in guardians.items():    
                    if 'guardians' in k:   
                        guardians[k] = (v).split('and') 
                        
        
        def exp_players():
            """copies the players with Experience and Inexperience and splits them into two lists
            """
            for experience in players_mod:
                for k,v in experience.items():
                    if 'experience' in k:
                        if v == True:
                            exper_players.append(experience)
                        elif v == False:
                            non_exper_players.append(experience)
                            """Randomly shuffles the list of Experience and Inexperience players"""
            random.shuffle(exper_players)
            random.shuffle(non_exper_players)
    
        
        def exit_stats():
            """If user enters 2 to exit then say good bye and exit app"""
            print("\n""Thank you for using the BASKETBALL TEAM STATS TOOL, see y'all next time.""\n")
            sys.exit()
            
        
        def main_menu():
            """ Main Menu, User can decide to see team stats to exit"""
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
            
    
    
    



    