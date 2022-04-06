# -*- coding: utf-8 -*-
class Game:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        
    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.P1Score()
        else:
            self.P2Score()

    
    def score(self):

        result = ""

        player_1_result = ""
        player_2_result = ""

        minus_result = self.player1_points - self.player2_points

        DEUCE = "Deuce"
        LOVE = "Love"
        FIFTEEN = "Fifteen"
        THIRTY = "Thirty"
        FORTY = "Forty"
        ADVANTAGE = "Advantage "
        WIN_FOR = "Win for "
        
        

        if (self.tied_game() and self.player1_points < 3):
            if (self.player1_points == 0):
                result = LOVE+"All"

            elif (self.player1_points == 1):
                result = FIFTEEN+"All"

            else:
                result = THIRTY+"All"
                
        if (self.tied_game() and self.player1_points > 2):
            result = DEUCE
        

        if (self.player1_points > 0 and self.player2_points == 0):
            if (self.player1_points == 1):
                player_1_result = FIFTEEN

            elif (self.player1_points == 2):
                player_1_result = THIRTY

            else:
                player_1_result = FORTY
            
            player_2_result = LOVE
            result = player_1_result + "-" + player_2_result

        if (self.player2_points > 0 and self.player1_points == 0):
            if (self.player2_points == 1):
                player_2_result = FIFTEEN

            elif (self.player2_points == 2):
                player_2_result = THIRTY

            else:
                player_2_result = FORTY
            
            player_1_result = LOVE
            result = player_1_result + "-" + player_2_result
        
        
        if (player_1_advantage and self.player1_points < 4):
            if (self.player1_points == 2):
                player_1_result = THIRTY

            elif (self.player1_points == 3):
                player_1_result = FORTY

            elif (self.player2_points == 1):
                player_2_result = FIFTEEN

            elif (self.player2_points == 2):
                player_2_result = THIRTY

            result = player_1_result + "-" + player_2_result

        if (player_2_advantage and self.player2_points < 4):
            if (self.player2_points == 2):
                player_2_result = THIRTY

            elif (self.player2_points == 3):
                player_2_result = FORTY

            elif (self.player1_points == 1):
                player_1_result = FIFTEEN

            elif (self.player1_points == 2):
                player_1_result = THIRTY

            result = player_1_result + "-" + player_2_result
        
        if self.game_over():
            result = WIN_FOR + self.current_player_advantage

        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.player1_points += 1
    
    def P2Score(self):
        self.player2_points += 1

    def tied_game(self):
        return self.player1_points == self.player2_points

    def game_over(self):
        return self.player1_points >= 4 or self.player2_points >= 4
    
    def current_player_advantage(self):
        if self.player1_points > self.player2_points:
            player_advantage = self.player1_name
        else:
            player_advantage = self.player2_name

        return player_advantage