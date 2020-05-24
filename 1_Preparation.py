#How many players
nb_players = HowManyPlayers()

#Who is playing?
for i in range(nb_players.nb):
    WhoAreYou(i)

#Shuffling the cards
deck = cards_game()

if nb_players.nb == 2:
    deck.cards_list = shuffle_deck(deck.cards_list)[:-10] 
else:
    deck.cards_list = shuffle_deck(deck.cards_list)

if len(deck.cards_list) % nb_players.nb != 0:
    deck.last_cards = deck.cards_list[-1]
    deck.cards_list = deck.cards_list[:-1]



#Distribution of the cards
nb_players.hmp()
    
for i in Player.players_list:
    i.myname()
    
    if i.player_number < nb_players.nb:
        i.cards = np.unique(list(np.sort(deck.cards_list[:len(deck.cards_list)//nb_players.nb*nb_players.nb].reshape(len(deck.cards_list)//nb_players.nb,nb_players.nb)[:,i.player_number])), return_counts=True)
        i.cave = (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine', 
                            'Shiva', 'Taurus'], dtype='<U9'), np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype='int64'))
    else:
        i.cards = np.unique(list(np.sort(np.append(deck.cards_list[:len(deck.cards_list)//nb_players.nb*nb_players.nb].reshape(len(deck.cards_list)//nb_players.nb,nb_players.nb)[:,i.player_number],deck.last_cards))), return_counts=True)
        i.cave = (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine', 
                            'Shiva', 'Taurus'], dtype='<U9'), np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype='int64'))
        
    print(i.cards)
    print(i.cave)   

#Choose who start
dice = dice(0,Player.players_list)
dice.random_choose()
dice.who_start()

#Initialize Counter
start_ind = 1
counter_turnZ = counter_turn(start_ind, nb_players.listing[dice.winner], (nb_players.listing[dice.winner]+1)%len(nb_players.listing))

#initialize Data Save
column_names = ["turn", "picker_number", "picker_name", "caller_number", "caller_name", "picker_cards", "picker_call", "caller_choose", "winner", "loser"]
myMatrix = pd.DataFrame(columns = column_names)

while len(Player.players_list) > 1:
    
    #THE GAME
    turn_startZ = turn_start(counter_turnZ.counter,counter_turnZ.winner,Player.players_list)  
    turn_startZ.which_turn()
    
    
    ##pick & announce
    if Player.players_list[counter_turnZ.winner].IA == "Bot" :
        card_picked = one_turn_IA_picked(counter_turnZ.counter, counter_turnZ.winner)
        card_announced = one_turn_IA_announce(counter_turnZ.counter, counter_turnZ.winner)²
    else:
        card_picked = one_turn_human_picked(counter_turnZ.counter, counter_turnZ.winner)
        card_announced = one_turn_human_announce(counter_turnZ.counter, counter_turnZ.winner) 
        
    turn_pickerZ = turn_picker(counter_turnZ.winner,Player.players_list, card_picked, card_announced)  
    turn_pickerZ.turn_picker_call()
        
    
    
    ##guess
    if Player.players_list[counter_turnZ.rival].IA == "Bot" :
        choice_made = one_turn_IA_guess(counter_turnZ.counter,counter_turnZ.rival)
        
    else:
        choice_made = one_turn_human_guess(counter_turnZ.counter, counter_turnZ.rival)
    
    
    turn_callerZ = turn_caller(counter_turnZ.rival,Player.players_list, choice_made)  
    turn_callerZ.turn_caller_call()    
        
    
    ##winner
    who_wonZ = who_won(counter_turnZ.winner,counter_turnZ.rival,Player.players_list,card_picked, card_announced,choice_made) 
    who_wonZ.tellwhowon()    
    
    show_winner(counter_turnZ.counter, who_wonZ.showwhowon())
    
    ##players Update
    topage_cards = np.where(Player.players_list[counter_turnZ.winner].cards[0] == card_picked)[0][0]
    topage_cave = np.where(Player.players_list[who_wonZ.return_loser()].cave[0] == card_picked)[0][0]
    
    Player.players_list[counter_turnZ.winner].cards[1][topage_cards] = Player.players_list[counter_turnZ.winner].cards[1][topage_cards] -1
    Player.players_list[who_wonZ.return_loser()].cave[1][topage_cave] = Player.players_list[who_wonZ.return_loser()].cave[1][topage_cave] + 1
    
    for i in Player.players_list:
        i.myname()
        
        print(i.cards)
        print(i.cave)
    
    ##Data Update
    myMatrix_temp = pd.DataFrame([[turn_startZ.turn_num,counter_turnZ.winner,Player.players_list[counter_turnZ.winner].name,(counter_turnZ.winner+1)%len(Player.players_list),Player.players_list[(counter_turnZ.winner+1)%len(Player.players_list)].name,card_picked, card_announced,choice_made,who_wonZ.return_winner(), who_wonZ.return_loser()]],columns = column_names)
    myMatrix = myMatrix.append(myMatrix_temp, ignore_index=True)   
    
    #Eliminate losers
    new_starter = who_wonZ.return_loser()
    nb_players.listing, new_starter  = ifloser_die(counter_turnZ.counter,  who_wonZ.return_winner(),  who_wonZ.return_loser(), Player.players_list, nb_players.listing)    
    
    nb_players.listing
    print(nb_players.listing)
    for i in Player.players_list:
        i.myname()
        
        print(i.cards)
        print(i.cave)
    
    ##Next Turn
    counter_turnZ = counter_turn(counter_turnZ.counter+1, new_starter,(nb_players.listing[new_starter]+1)%len(nb_players.listing))
   