import random

# Implement a basic Snakes and ladders game including 2 players. Using OOP concepts.

# My unique rolls, each player will keep track of total rolls taken of dice to win the game. The player doesnt have to roll a perfect number to finish, as long as they can get to the last block
# Snakes: snake head being key and tail being value {10: 2, 7: 4, 21: 13, 24:6, 33:19}
# Game runs automatically, recording how many rolls each player took to finish the game

class Game():

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def player_move(self, player):
        roll = random.randint(1,6)
        player.move(roll)
        self.board.check_snakes(player)
        self.board.check_ladders(player)
        #self.board.check_win(player)


class Player():

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.roll_count = 0

    def move(self, steps):
        self.position += steps

        if self.position >= 34:
            self.position = 34

        self.roll_count += 1




class Board():

    def __init__(self, size = 34):
        self.snakes = {10: 2, 7: 4, 21: 13, 24:6, 33:19}    # Key is snake head and value is tail
        self.ladders = {1: 12, 5: 16, 11:22, 15: 23, 20: 31} # Key is ladder bottom and value is top
        self.size = size

    def check_snakes(self, player):
        if player.position in self.snakes.keys():
            player.position = self.snakes[player.position]
    
    def check_ladders(self, player):
        if player.position in self.ladders.keys():
            player.position = self.ladders[player.position]
    
    def check_win(self, player):
        if player.position == 34:
            return True
        else: 
            return False
        


    
board = Board()
player1 = Player("Player1")
player2 = Player("Player2")
game = Game(player1, player2, board)

'''while True:
    # Player 1's turn
    game.player_move(player1)
    if board.check_win(player1):  # Check if Player 1 wins
        winner = player1
        print(f"{winner.name} wins!")
        break

    # Player 2's turn
    game.player_move(player2)
    if board.check_win(player2):  # Check if Player 2 wins
        winner = player2
        print(f"{winner.name} wins!")
        break

print(f"Player1 took {player1.roll_count} rolls to finish the game")
print(f"Player2 took {player2.roll_count} rolls to finish the game")'''

totalPlayer1 = 0
totalPlayer2 = 0
totalWin1 = 0
totalWin2 = 0

simulationCount = 10000

for i in range(simulationCount):
    # Reset player1's position and roll count for each simulation
    player1.position = 0
    player1.roll_count = 0

    player2.position = 6        # Player 2 starts at position 6 for fair chance of winning
    player2.roll_count = 0

    while True:
        # Player 1's turn
        game.player_move(player1)
        if board.check_win(player1):  # Check if Player 1 wins
            totalPlayer1 += player1.roll_count  # Add the roll count for this simulation
            totalPlayer2 += player2.roll_count  # Add the roll count for this simulation
            totalWin1 += 1
            break

        # Player 2's turn
        game.player_move(player2)
        if board.check_win(player2):  # Check if Player 2 wins
            totalPlayer1 += player1.roll_count  # Add the roll count for this simulation
            totalPlayer2 += player2.roll_count  # Add the roll count for this simulation
            totalWin2 += 1
            break

print(f"After 10000 simulations, player 1 took an average of {(totalPlayer1/simulationCount):.2f} rolls to complete the game")
print(f"With {totalWin1} wins")
print(f"After 10000 simulations, player 2 took an average of {(totalPlayer2/simulationCount):.2f} rolls to complete the game")
print(f"With {totalWin2} wins")

# calculate average rolls for combined rolls
print(f"Average rolls for both players is {(totalPlayer1 + totalPlayer2)/(simulationCount):.2f}")

#two player game, what is the probability that player 1 wins
print(f"Probability that player 1 wins is {((totalWin1/simulationCount)*100):.2f}%")
    




    

