# Initialisation du jeu

##Nombre de joueurs
Nb_players = nb_players(nb=2, listing = np.arange(0,2))

#xxx Nb_players.nb
#xxx> 2

##Definition des joueurs

Player1 = Player(name = "Joueur_1", player_number = 0)
Player2 = Player(name = "Joueur_2", player_number = 1)
Players_list = [Player1,Player2]

#xxx Player.players_list[0].name
#xxx> 'Joueur_1'

##Mélange des cartes (fonctionne si plus de 2 joueurs)
Deck = cards_game()

#xxx Deck.cards_list
if Nb_players.nb == 2:
    Deck.cards_list = shuffle_deck(Deck.cards_list)[:-10] 
else:
    Deck.cards_list = shuffle_deck(Deck.cards_list)

if len(Deck.cards_list) % Nb_players.nb != 0:
    Deck.last_cards = Deck.cards_list[-1]
    Deck.cards_list = Deck.cards_list[:-1]
    

##Distribution des cartes (fonctionne si plus de 2 joueurs)
for i in Players_list:
    df1 = pd.DataFrame({'key': ['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine','Shiva', 'Taurus']})
    
    if i.player_number < Nb_players.nb:
        tempx = np.unique(list(np.sort(Deck.cards_list[:len(Deck.cards_list)//Nb_players.nb*Nb_players.nb].reshape(len(Deck.cards_list)//Nb_players.nb,Nb_players.nb)[:,i.player_number])), return_counts=True)
        df2 = pd.DataFrame({'key': tempx[0],
                            'value': tempx[1]})
        df = df1.merge(df2, on='key', how='left').fillna(0)
        df['value'] = df['value'].apply(np.int64)
        
        i.cards = (np.array(df['key'], dtype='<U9'), np.array(df['value'], dtype='int64'))
        i.cave = (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine', 
                            'Shiva', 'Taurus'], dtype='<U9'), np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype='int64'))
    else:
        tempx = np.unique(list(np.sort(np.append(Deck.cards_list[:len(Deck.cards_list)//Nb_players.nb*Nb_players.nb].reshape(len(Deck.cards_list)//Nb_players.nb,Nb_players.nb)[:,i.player_number],Deck.last_cards))), return_counts=True)
        
        df2 = pd.DataFrame({'key': tempx[0],
                            'value': tempx[1]})
        df = df1.merge(df2, on='key', how='left').fillna(0)
        df['value'] = df['value'].apply(np.int64)
        
        i.cards = (np.array(df['key'], dtype='<U9'), np.array(df['value'], dtype='int64'))
        i.cave = (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine', 
                            'Shiva', 'Taurus'], dtype='<U9'), np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype='int64'))
    
        
## Qui commence
##On lance le dé

de = dice(0,Players_list)
de.random_choose()

#xxx de.winner
#xxx> 0 ou 1 si 2 joueurs

#Initialize Counter
start_ind = 1
compteur_tour = round_nb(start_ind, Nb_players.listing[de.winner], (Nb_players.listing[de.winner]+1)%len(Nb_players.listing))

#xxx compteur_tour.player_start
#xxx> 1

#Initialize Game status
game_end = False

#Initialize Reward
Reward = 0

#Initialize Actions
RL_actions = np.array([[1,0,1,0,0,0,0,0,0,0],
                       [1,0,0,1,0,0,0,0,0,0],
                       [1,0,0,0,1,0,0,0,0,0],
                       [1,0,0,0,0,1,0,0,0,0],
                       [1,0,0,0,0,0,1,0,0,0],
                       [1,0,0,0,0,0,0,1,0,0],
                       [1,0,0,0,0,0,0,0,1,0],
                       [1,0,0,0,0,0,0,0,0,1],
                       [0,1,1,0,0,0,0,0,0,0],
                       [0,1,0,1,0,0,0,0,0,0],
                       [0,1,0,0,1,0,0,0,0,0],
                       [0,1,0,0,0,1,0,0,0,0],
                       [0,1,0,0,0,0,1,0,0,0],
                       [0,1,0,0,0,0,0,1,0,0],
                       [0,1,0,0,0,0,0,0,1,0],
                       [0,1,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0],
                       [0,1,0,0,0,0,0,0,0,0]
                       ])

RL_pick_actions_proba = np.array([1/16,1/16,1/16,1/16,
                                  1/16,1/16,1/16,1/16,
                                  1/16,1/16,1/16,1/16,
                                  1/16,1/16,1/16,1/16,
                                  0,0])


RL_call_actions_proba = np.array([0,0,0,0,
                                  0,0,0,0,
                                  0,0,0,0,
                                  0,0,0,0,
                                  1/2,1/2]) 

#Initialisation Action
prob =  np.zeros(18)
if compteur_tour.player_start != 0:
    prob = RL_call_actions_proba
else:
    prob = RL_pick_actions_proba
    
action =  np.zeros(18)