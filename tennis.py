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

        SCORE = [{
            0: LOVE,
            1: FIFTEEN,
            2: THIRTY,
            3: FORTY
        }]
        
        def current_game(self):
            self._current_game
            if self.tied_game() and self.player1_points < 3:
                if self.player1_points == SCORE[self.player1_points]:
                    result = SCORE[self.player1_points]+"All"
                else:
                    result = DEUCE
            return self._current_game = result
                

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
        
        
        def advantage_game(self):
            self._advantage_game =  self.player1_points > self.player2_points or self.player2_points > self.player1_points
            if (self._advantage_game and self.current_player_advantage() < 4):
                if (self.player1_points == SCORE[self.player1_points]):
                    player_1_result = SCORE[self.player1_points]
                else:
                    player_2_result = SCORE[self.player2_points] 

            result = player_1_result + "-" + player_2_result

            return result
        
        if self.game_over():
            result = WIN_FOR + self.current_player_advantage

    
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