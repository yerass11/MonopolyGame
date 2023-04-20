from aspects.store import chance, community, board, property_info, utilities, properties
from aspects.player import Player

import time

chance_set = list(chance.values())
community_set = list(community.values())

class Board:
    def __init__(self, player_count=4, log=True):
        self.players = []

        # Card piles
        self.chance_set = chance_set
        self.community_set = community_set

        # Houses and Hotels in the bank
        self.houses = 32
        self.hotels = 12

        # Places on the board
        self.squares = board
        self.utilities = utilities

        info = property_info
        for item in info:
            item.update({"owned":None, "houses": 0, "hotel": False})

        self.properties = dict(zip(properties, info))
        self.log_ = log
        
        for _ in range(player_count):
            Player(self)
    
    def log(self, text):
        if self.log_:
            print(text)

    def add_player(self, player):
        self.log("Loaded in player %s" % str(player.player_id + 1))
        self.players.append(player)

    def do_turn(self):
        for p in self.players:
            p.play()

    def play(self, turns=150):
        for _ in range(turns):
            left_in_game = list(filter(lambda x: x.status != 0, self.players))
            if len(left_in_game) != 1:
                self.do_turn()
            else:
                return self.log("Player %s won the game" % str(left_in_game[0].player_id + 1))