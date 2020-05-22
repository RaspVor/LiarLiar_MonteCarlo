import random
import numpy as np
import numpy.random
import pandas as pd

class nb_players:
    def __init__(self, nb=2, listing = np.array([])):
        self.nb=nb
        self.listing=listing

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

# Initialisation du jeu

##Nombre de joueurs
Nb_players = nb_players(nb=2)

Nb_players.nb
#xxx> 2


#Mélange des cartes
Deck = cards_game()

#xxx Deck.cards_list