# Python-Coding-Projects
This Repository will hold all my Python Coding Projects

In the Folder 'Technical Questions', you will find 2 algorithms:

**Algorithm Trading**: This algorithm goes alongside the 'data.csv' file. The point of this algorithm is to implement a simple trading algorrithm to decide which stocks to buy. The main strategy is that whenever a share drops in value by 3%, you buy-in and sell 5 days later.

Assumptions:
* You do not incur any transaction fees when buying or selling
* Assume the data contains only valid trading days
* The data is ordered by company and date (oldest first)
* You buy and sell at the end of the day
* If the price dropped by 3% on day 5 you still sell and don’t buy again

Goals:
* For SOL-za, what is the return over the period?
* What is the min, max and average return for all the companies over the period?
* If the decide to only by buy the share dropped by 4% or more, what is the return in this case for each
company?
* If the decide to hold for 10 days, what is the return in this case for each company? (with a 3% drop)
* From the results above, do you expect this strategy to be successful going forward?

**Snakes & Ladders**: This algorithm simply implements a simulation of 2 players playing a game of Snakes & Ladders. Refer to the image 'Board State.png' file for a visual view of the board state. This simulation is run 10,000 times to get an accurate assumption.

Goals
* If you played the game by yourself, what is the average number of rolls required to finish?
* In a two person game, what is the average number of combined rolls by both players required for the
game to finish?
* In a two person game, what is the probability that Player 1 wins?
* You decide you want the game to have approximately fair odds, and you do this by changing the square
that Player 2 starts on. From the options below, which square for Player 2’s start position gives the
closest to equal odds for both players?



