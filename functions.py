# Fonctions

#Mélanger le jeu de cartes
def shuffle_deck(deck):
    deck_copy = deck
    np.random.shuffle(deck_copy)
    return(deck_copy)


def one_turn_Bot_picker_Action(player):
    #exemple player =  Players_list[1]
    
    Picker_options = np.minimum([1,1,1,1,1,1,1,1], player.cards[1])
    temp = len(Picker_options[Picker_options>0])
    
    proba=[1/temp,1/temp,1/temp,1/temp,1/temp,1/temp,1/temp,1/temp]
    Picker_options = Picker_options*proba

    
    IA_pick_choice = np.random.choice(8, size=1, p=Picker_options)[0]
    
    Action_pickerpick_list = np.array([[1,0,0,0,0,0,0,0],
                                       [0,1,0,0,0,0,0,0],
                                       [0,0,1,0,0,0,0,0],
                                       [0,0,0,1,0,0,0,0],
                                       [0,0,0,0,1,0,0,0],
                                       [0,0,0,0,0,1,0,0],
                                       [0,0,0,0,0,0,1,0],
                                       [0,0,0,0,0,0,0,1]]
                                      )
    
    IA_pick_call = np.random.choice(2, size=1, p=[1/6,5/6])[0]  
    
    Action_pickercall_list = np.array([[1,0],[0,1]])
      
    return(Action_pickerpick_list[IA_pick_choice],
           Action_pickercall_list[IA_pick_call],
           np.append(Action_pickercall_list[IA_pick_call],Action_pickerpick_list[IA_pick_choice]))

#xxx one_turn_Bot_picker_Action(Players_list[0].cards[1])
#xxx> (array([0, 0, 1, 0, 0, 0, 0, 0]),
#xxx> array([0, 1]),
#xxx> array([0, 1, 0, 0, 1, 0, 0, 0, 0, 0]))
       
       
def one_turn_Bot_caller_Action():
    
    IA_call_call = np.random.choice(2, size=1, p=[1/6,5/6])[0]  
    
    Action_callercall_list = np.array([[1,0],[0,1]])
    
    return(Action_callercall_list[IA_call_call])

#xxx one_turn_Bot_caller_Action()
#xxx> array([1, 0])

#Control des probas
def get_probs_pick_actions(Q_s, epsilon, nS = 16, nA=18):
    """ obtains the action probabilities corresponding to epsilon-greedy policy """
    policy_s = np.ones(nA) * epsilon / nS
    best_a = np.argmax(Q_s[:-2])
    policy_s[best_a] = 1 - epsilon + (epsilon / nS)
    
    selector = np.array([1,1,1,1,
                         1,1,1,1,
                         1,1,1,1,
                         1,1,1,1,
                         0,0])
    policy_s = np.where(selector==0, 0, policy_s)
    
    return policy_s


def get_probs_call_actions(Q_s, epsilon, nS = 2, nA=18):
    """ obtains the action probabilities corresponding to epsilon-greedy policy """
    policy_s = np.ones(nA) * epsilon / nS
    best_a = np.argmax(Q_s[-2:])+16
    policy_s[best_a] = 1 - epsilon + (epsilon / nS)
    
    selector = np.array([0,0,0,0,
                         0,0,0,0,
                         0,0,0,0,
                         0,0,0,0,
                         1,1])
    policy_s = np.where(selector==0, 0, policy_s)
    
    return policy_s