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
        if (self.player1Points == self.player2Points and self.player1Points < 3):
            if (self.player1Points == 0):
                result = "Love-All"
            if (self.player1Points == 1):
                result = "Fifteen-All"
            if (self.player1Points == 2):
                result = "Thirty-All"
                
        if (self.player1Points == self.player2Points and self.player1Points > 2):
            result = "Deuce"
        
        player_1_result = ""
        player_2_result = ""
        if (self.player1Points > 0 and self.player2Points == 0):
            if (self.player1Points == 1):
                player_1_result = "Fifteen"
            if (self.player1Points == 2):
                player_1_result = "Thirty"
            if (self.player1Points == 3):
                player_1_result = "Forty"
            
            player_2_result = "Love"
            result = player_1_result + "-" + player_2_result
        if (self.player2Points > 0 and self.player1Points == 0):
            if (self.player2Points == 1):
                player_2_result = "Fifteen"
            if (self.player2Points == 2):
                player_2_result = "Thirty"
            if (self.player2Points == 3):
                player_2_result = "Forty"
            
            player_1_result = "Love"
            result = player_1_result + "-" + player_2_result
        
        
        if (self.player1Points > self.player2Points and self.player1Points < 4):
            if (self.player1Points == 2):
                player_1_result="Thirty"
            if (self.player1Points == 3):
                player_1_result="Forty"
            if (self.player2Points == 1):
                player_2_result="Fifteen"
            if (self.player2Points == 2):
                player_2_result="Thirty"
            result = player_1_result + "-" + player_2_result
        if (self.player2Points > self.player1Points and self.player2Points < 4):
            if (self.player2Points == 2):
                player_2_result="Thirty"
            if (self.player2Points == 3):
                player_2_result="Forty"
            if (self.player1Points == 1):
                player_1_result="Fifteen"
            if (self.player1Points == 2):
                player_1_result="Thirty"
            result = player_1_result + "-" + player_2_result
        
        if (self.player1Points > self.player2Points and self.player2Points >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.player2Points > self.player1Points and self.player1Points >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.player1Points >= 4 and self.player2Points >= 0 and (self.player1Points - self.player2Points) >=2 ):
            result = "Win for " + self.player1Name
        if (self.player2Points >= 4 and self.player1Points >= 0 and (self.player2Points - self.player1Points) >=2 ):
            result = "Win for " + self.player2Name
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