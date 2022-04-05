# -*- coding: utf-8 -*-
class Game:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Points = 0
        self.player2Points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

            

    
    def score(self):

        result = ""

        player_1_result = ""
        player_2_result = ""

        minus_result = self.player1Points - self.player2Points

        DEUCE = "Deuce"
        LOVE = "Love"
        FIFTEEN = "Fifteen"
        THIRTY = "Thirty"
        FORTY = "Forty"
        ADVANTAGE = "Advantage "
        WIN_FOR = "Win for "

        if (self.player1Points == self.player2Points and self.player1Points < 3):
            if (self.player1Points == 0):
                result = LOVE+"All"

            if (self.player1Points == 1):
                result = FIFTEEN+"All"

            if (self.player1Points == 2):
                result = THIRTY+"All"
                
        if (self.player1Points == self.player2Points and self.player1Points > 2):
            result = DEUCE
        

        if (self.player1Points > 0 and self.player2Points == 0):
            if (self.player1Points == 1):
                player_1_result = FIFTEEN

            if (self.player1Points == 2):
                player_1_result = THIRTY

            if (self.player1Points == 3):
                player_1_result = FORTY
            
            player_2_result = LOVE
            result = player_1_result + "-" + player_2_result

        if (self.player2Points > 0 and self.player1Points == 0):
            if (self.player2Points == 1):
                player_2_result = FIFTEEN

            if (self.player2Points == 2):
                player_2_result = THIRTY

            if (self.player2Points == 3):
                player_2_result = FORTY
            
            player_1_result = LOVE
            result = player_1_result + "-" + player_2_result
        
        
        if (self.player1Points > self.player2Points and self.player1Points < 4):
            if (self.player1Points == 2):
                player_1_result = THIRTY

            if (self.player1Points == 3):
                player_1_result = FORTY

            if (self.player2Points == 1):
                player_2_result = FIFTEEN

            if (self.player2Points == 2):
                player_2_result = THIRTY

            result = player_1_result + "-" + player_2_result

        if (self.player2Points > self.player1Points and self.player2Points < 4):
            if (self.player2Points == 2):
                player_2_result = THIRTY

            if (self.player2Points == 3):
                player_2_result = FORTY

            if (self.player1Points == 1):
                player_1_result = FIFTEEN

            if (self.player1Points == 2):
                player_1_result = THIRTY

            result = player_1_result + "-" + player_2_result
        
        if (self.player1Points > self.player2Points and self.player2Points >= 3):
            result = ADVANTAGE + self.player1Name
        
        if (self.player2Points > self.player1Points and self.player1Points >= 3):
            result = ADVANTAGE + self.player2Name
        
        if (self.player1Points >= 4 and self.player2Points >= 0 and minus_result >=2 ):
            result = WIN_FOR + self.player1Name
        if (self.player2Points >= 4 and self.player1Points >= 0 and minus_result >=2 ):
            result = WIN_FOR + self.player2Name
        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.player1Points += 1
    
    
    def P2Score(self):
        self.player2Points += 1