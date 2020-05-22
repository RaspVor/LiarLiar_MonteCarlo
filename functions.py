def shuffle_deck(deck):
    deck_copy = deck
    np.random.shuffle(deck_copy)
    return(deck_copy)


def HowManyPlayers():
    
    
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    layout = [  [sg.Text('How many summoners?')],
                [sg.Text('Give me a number'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            print(values[0], "challengers will compete")
            break
    
    window.close()
    
    return(nb_players(int(values[0]),np.arange(0,int(values[0]))))
    

def WhoAreYou(num=int):
    sg.ChangeLookAndFeel('GreenTan')
    # All the stuff inside the window.
    layout = [  [sg.Text('My Lord,')],
                [sg.Text('What is your summoner name?'), sg.InputText()],
                [sg.Text('Are your a human?'), sg.Radio('I am a human!     ', "RADIO1"), sg.Radio('I am a ROBOT!    ', "RADIO1", default=True)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Introduce yourself!', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        
        player_statut = "as an IA!"
        player_statut_official = "Bot"
        
        if values[1] == True:
            player_statut = "as a humanoid!"
            player_statut_official = "Human"

            
        print(values[0], "has joined the game", player_statut)
        break
    
    window.close()
    layout = None
    window = None
    gc.collect()
        
    Player(values[0], player_statut_official, num)
    
    
def one_turn_human_announce(turn_number, past_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    radio_choices = list(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine', 'Shiva', 'Taurus'])
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( Player.players_list[past_winner].name + ' makes a call. Choose a card !')],
                [sg.Radio(text, 1) for text in radio_choices],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            card_played_indZ = list(values.values()).index(True)
            card_playedZ = radio_choices[card_played_indZ]
            
            break
    
    window.close()
    layout = None
    window = None
    gc.collect()
    
    return(card_playedZ)


def one_turn_IA_announce(turn_number, past_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    IAchoice = np.random.choice(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine', 'Shiva', 'Taurus'],1)[0]
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( 'Me, ' + Player.players_list[past_winner].name + '! I summon ' + IAchoice)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
        
            card_playedZ = IAchoice
            break
    
    window.close()
    layout = None
    window = None
    gc.collect()
    
    return(card_playedZ)



 
def one_turn_human_picked(turn_number, past_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    radio_choices = Player.players_list[past_winner].cards[0][np.where(Player.players_list[past_winner].cards[1] > 0 )[0]]
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( Player.players_list[past_winner].name + ' pick a card !')],
                [sg.Radio(text, 1) for text in radio_choices],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            card_played_indZ = list(values.values()).index(True)
            card_playedZ = radio_choices[card_played_indZ]
            
            break
    
    window.close()
    layout = None
    window = None
    gc.collect()
    
    return(card_playedZ)



def one_turn_IA_picked(turn_number, past_winner):
    #sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    IAchoice = np.random.choice(Player.players_list[past_winner].cards[0][np.where(Player.players_list[past_winner].cards[1] > 0 )[0]],1)[0]
    
    #layout = [  [sg.Text('Round ' + str(turn_number))],
    #            [sg.Text( 'Me, ' + Player.players_list[past_winner].name + '! I pick ' + IAchoice)],
    #            [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    #window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    #while True:
    #    event, values = window.read()
    #    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
    #        break
    #    if event in ('Ok'):   # if user closes window or clicks cancel
        
    card_playedZ = IAchoice
    #        break
    
    #window.close()
    #layout = None
    #window = None
    #gc.collect()
        
    return(card_playedZ)    





def one_turn_human_guess(turn_number, after_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    radio_choices = ["TRUE", "FALSE"]
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( Player.players_list[after_winner].name + '. Make a choice!')],
                [sg.Radio(text, 1) for text in radio_choices],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            choice_indZ = list(values.values()).index(True)
            choiceZ = radio_choices[choice_indZ]
            
            break
    
    window.close()
    layout = None
    window = None
    gc.collect()
        
    return(choiceZ)


def one_turn_IA_guess(turn_number, after_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    IAchoice =  np.random.choice(["TRUE", "FALSE"],1)[0]
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( 'Me, ' + Player.players_list[after_winner].name + '! I say it is ' + IAchoice)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            choiceZ = IAchoice
            
            break
    
    window.close()
    layout = None
    window = None
    gc.collect()
        
    return(choiceZ)


def show_winner(turn_number, text):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text(text)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel', 'Ok'):   # if user closes window or clicks cancel
            break
    
    window.close()
    layout = None
    window = None
    gc.collect()
    
def ifloser_die(turn_number, winner_num, loser_num, players_list, nb_players):
    new_starter = loser_num
    
    if (np.where(players_list[loser_num].cave[1] > 3)[0].size != 0) or (np.where(players_list[loser_num].cards[1] < 1)[0].size == 8):
        
        sg.ChangeLookAndFeel('DarkAmber')
        # All the stuff inside the window.
        
        IAchoice =  np.random.choice(["TRUE", "FALSE"],1)[0]
        
        
        layout = [  [sg.Text('Round ' + str(turn_number))],
                    [sg.Text( players_list[loser_num].name + ' is eliminated! Go to hell!!')],
                    [sg.Button('Ok'), sg.Button('Cancel')] ]
    
        # Create the Window
        window = sg.Window('Summoners! Rise Up', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event in (None, 'Cancel','Ok'):   # if user closes window or clicks cancel
                break
        
        window.close()
        layout = None
        window = None
        gc.collect()
        
        players_list.pop(loser_num)
        
        new_starter = np.where(np.delete(nb_players, np.where(nb_players == loser_num)) == winner_num)[0][0]
        
        return(np.arange(0,len(nb_players)-1), new_starter)
    else:
        return(np.arange(0,len(nb_players)), new_starter)
