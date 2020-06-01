# Class

class nb_players:
    def __init__(self, nb=2, listing = np.array([])):
        self.nb=nb
        self.listing=listing

class Player:

    def __init__(self, name = "Anonymous", player_number = int, cards = list(), cave = list()):
        self.name = name
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

class dice:
    def __init__(self, winner = 0, players_list = []):
        self.winner = winner
        self.players_list = players_list
    
    def random_choose(self):
        self.winner = random.randint(1,len(self.players_list))-1
    


class round_nb:
    def __init__(self, round_num = 1, player_start = 0, player_next = 0):  
        self.round_num = round_num
        self.player_start = player_start
        self.player_next = player_next