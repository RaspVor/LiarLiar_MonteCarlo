#Class

#
class nb_players:
    def __init__(self, nb=2, listing = np.array([])):
        self.nb=nb
        self.listing=listing
        



class Player:
    
    def __init__(self, name = "Anonymous", IA = "Bot", player_number = int, cards = list(), cave = list()):
        self.name = name
        self.IA = IA
        self.player_number = player_number
        self.cards = cards
        self.cave = cave
    

class cards_game:
    def __init__(self, cards_list = np.array(["Ifrit","Ifrit","Ifrit","Ifrit","Ifrit","Ifrit","Ifrit","Ifrit",
                                              "Shiva","Shiva","Shiva","Shiva","Shiva","Shiva","Shiva","Shiva",
                                              "Ondine","Ondine","Ondine","Ondine","Ondine","Ondine","Ondine","Ondine",
                                              "Ahuri","Ahuri","Ahuri","Ahuri","Ahuri","Ahuri","Ahuri","Ahuri",
                                              "Bahamut","Bahamut","Bahamut","Bahamut","Bahamut","Bahamut","Bahamut","Bahamut",
                                              "Leviathan","Leviathan","Leviathan","Leviathan","Leviathan","Leviathan","Leviathan","Leviathan",
                                              "Golgotha","Golgotha","Golgotha","Golgotha","Golgotha","Golgotha","Golgotha","Golgotha",
                                              "Taurus","Taurus","Taurus","Taurus","Taurus","Taurus","Taurus","Taurus"]),
                       last_cards=np.array([])
                 ):
        self.cards_list = cards_list
        self.last_cards = last_cards


class card_played:
    def __init__(self, card = "ERROR"):
        self.card=card
        
class card_announced:
    def __init__(self, card = "ERROR"):
        self.card=card
        
class card_guessed:
    def __init__(self, card = "ERROR"):
        self.card=card

        

class dice:
    def __init__(self, winner = 0, players_list = []):
        self.winner = winner
        self.players_list = players_list
    
    def random_choose(self):
        self.winner = random.randint(1,len(self.players_list))-1
    


class counter_turn:
    def __init__(self, counter = 1, winner = 0, rival = 0):  
        self.counter = counter
        self.winner = winner
        self.rival = rival

class turn_start:
    def __init__(self,turn_num = 1, player_number = 0, players_list = []):
        self.turn_num = turn_num
        self.player_number = player_number
        self.players_list = players_list
    


class turn_picker:
    def __init__(self, player_number = 0, players_list = [], picker_cards = "ERROR", picker_call = "ERROR"):
        self.player_number = player_number
        self.players_list = players_list
        self.picker_cards = picker_cards
        self.picker_call = picker_call
    


class turn_caller:
    def __init__(self, player_number = 0, players_list = [], caller_choose = "ERROR"):
        self.player_number = player_number
        self.players_list = players_list
        self.caller_choose = caller_choose
    


class who_won:
    def __init__(self, player_number = 0, rival_number = 0, players_list = [], picker_cards = "ERROR", picker_call = "ERROR", caller_choose = "ERROR"):
        self.player_number = player_number
        self.rival_number = rival_number
        self.players_list = players_list
        self.picker_cards = picker_cards
        self.picker_call = picker_call
        self.caller_choose = caller_choose


    def return_winner(self):
        if ((self.picker_cards == self.picker_call) and self.caller_choose == "TRUE") or ((self.picker_cards != self.picker_call) and self.caller_choose == "FALSE"):
            return (self.rival_number)
        else:
            return (self.player_number)
        
    def return_loser(self):
        if ((self.picker_cards == self.picker_call) and self.caller_choose == "TRUE") or ((self.picker_cards != self.picker_call) and self.caller_choose == "FALSE"):
            return (self.player_number)
        else:
            return (self.rival_number)

   