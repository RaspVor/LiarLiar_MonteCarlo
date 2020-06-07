# Déroulement du jeu

while (game_end == False):

    #print('Reward :',Reward)
    #print('compteur_tour.round_num :',compteur_tour.round_num)
    #print('compteur_tour.player_start :',compteur_tour.player_start)
    #print('Players_list[0].cards[1] :',Players_list[0].cards[1])
    #print('Players_list[0].cave[1] :',Players_list[0].cave[1])
    #print('Players_list[1].cards[1] :',Players_list[1].cards[1])
    #print('Players_list[1].cave[1] :',Players_list[1].cave[1])
    
    
    State = (str(compteur_tour.player_start)+str(Players_list[0].cards[1])+str(Players_list[0].cave[1])+str(Players_list[1].cards[1])+str(Players_list[1].cave[1]))
   
     
    if compteur_tour.player_start != 0:
        
        #Initialisation Action/prob
        prob = RL_call_actions_proba
        
        #IA pick
        turn_played_IA = one_turn_Bot_picker_Action(Players_list[compteur_tour.player_start])
        
        #The card picked is removed from his deck
        temp =  (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine','Shiva', 'Taurus'], dtype='<U9'), 
                 Players_list[compteur_tour.player_start].cards[1] - turn_played_IA[0])
        Players_list[compteur_tour.player_start].cards = temp
        
        #RL make a call
        RL_call_choice = np.random.choice(18, size=1, p=prob)[0]
        RL_call_action = RL_actions[RL_call_choice][:2]
        Action = RL_actions[RL_call_choice] #save the action
        
        #We check who won
        if ((RL_call_action == turn_played_IA[1]).all() == True):
            temp =  (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine','Shiva', 'Taurus'], dtype='<U9'), 
                     Players_list[compteur_tour.player_start].cave[1] + turn_played_IA[0])
            Players_list[compteur_tour.player_start].cave = temp
            compteur_tour = round_nb(compteur_tour.round_num +1 , compteur_tour.player_start, (compteur_tour.player_start+1)%len(Nb_players.listing))
        else:
            temp =  (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine','Shiva', 'Taurus'], dtype='<U9'), 
                     Players_list[compteur_tour.player_next].cave[1] + turn_played_IA[0])
            Players_list[compteur_tour.player_next].cave = temp
            compteur_tour = round_nb(compteur_tour.round_num +1 , compteur_tour.player_next, (compteur_tour.player_next+1)%len(Nb_players.listing))
        
        
        #Reward
        if (len(Players_list[compteur_tour.player_start].cards[1][Players_list[compteur_tour.player_start].cards[1] < 0]) > 0):
            game_end = True
            Reward = 10000
        elif (len(Players_list[compteur_tour.player_start].cave[1][Players_list[compteur_tour.player_start].cave[1] > 3]) > 0):
            game_end = True
            Reward = 10000
        elif (len(Players_list[compteur_tour.player_next].cave[1][Players_list[compteur_tour.player_next].cave[1] > 3]) > 0):
            game_end = True
            Reward = -10000
        elif ((RL_call_action == turn_played_IA[1]).all() == True):
            Reward = 10
        else:
            Reward = -10
        
        episode.append((State, str(Action), Reward))
        
    else:
        
        #Initialisation Action/prob
        prob = RL_pick_actions_proba
        
        #RL pick
        RL_pick_choice = np.random.choice(18, size=1, p=prob)[0]
        RL_pick_action = RL_actions[RL_pick_choice]
        
        #Card pick and call made
        RL_pickcard_action = RL_pick_action[2:10]
        RL_pickcall_action = RL_pick_action[:2]
        Action = RL_actions[RL_pick_choice] #save the action
        
        #The card picked is removed from his deck
        temp =  (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine','Shiva', 'Taurus'], dtype='<U9'), 
                 Players_list[compteur_tour.player_start].cards[1] - RL_pickcard_action)
        Players_list[compteur_tour.player_start].cards = temp
        
        #IA make a call
        IA_call_choice = one_turn_Bot_caller_Action()
        
        
        #We check who won
        if ((RL_pickcall_action ==  IA_call_choice).all() == True):
            temp = (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine','Shiva', 'Taurus'], dtype='<U9'), 
                    Players_list[compteur_tour.player_start].cave[1] + RL_pickcard_action)
            Players_list[compteur_tour.player_start].cave = temp
            compteur_tour = round_nb(compteur_tour.round_num +1 , compteur_tour.player_start, (compteur_tour.player_start+1)%len(Nb_players.listing))
        else:
            temp = (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine','Shiva', 'Taurus'], dtype='<U9'), 
                    Players_list[compteur_tour.player_next].cave[1] + RL_pickcard_action)
            Players_list[compteur_tour.player_next].cave = temp
            compteur_tour = round_nb(compteur_tour.round_num +1 , compteur_tour.player_next, (compteur_tour.player_next+1)%len(Nb_players.listing))
        
        #Reward
        if (len(Players_list[compteur_tour.player_start].cards[1][Players_list[compteur_tour.player_start].cards[1] < 0]) > 0):
            game_end = True
            Reward = -10000
        elif (len(Players_list[compteur_tour.player_start].cave[1][Players_list[compteur_tour.player_start].cave[1] > 3]) > 0):
            game_end = True
            Reward = -10000
        elif (len(Players_list[compteur_tour.player_next].cave[1][Players_list[compteur_tour.player_next].cave[1] > 3]) > 0):
            game_end = True
            Reward = 10000
        elif ((RL_pickcall_action ==  IA_call_choice).all() == True):
            Reward = -10
        else:
            Reward = 10
            
        episode.append((State, str(Action), Reward))
            
    