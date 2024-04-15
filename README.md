# Snake-and-Ladders-game-
Build a Python Script to play Snakes and Ladders versus two players.
In this project you will Implement a snakes and ladders game with two players. You will use a 10 by 10 table with ladders defined in positions as follows

1. You will use the random module to define the dice moves: typical dice has 1 to 6 combination of dots
2. The position initially is zero and you will update it with the value of the dice roll function return using the following idea:
3. For every players turn, for the dice roll be sure to print their current position and the dice roll return
4. Define the get_position function which will find the position of the player and place on the relevant snake and ladder combinations.
5. Define the dice roll function which takes the player, current position and updates this with the random dice roll result, returning the final position after roll
6. Define the snake and ladder function which depedning on the players positon moves them up and down with a message
7. Finally consolidate all into the play function which returns the result of the play.

Rules of the games are as follows.

        Welcome to Snake and Ladder Game.
        Version: 1.0.0  *Feel Free to use anything* 

                Rules:
          1. Initially all the players are at starting position i.e. 0. 
             Take it in turns to roll the dice. 
             Move forward the number of spaces shown on the dice.
          2. If you land at the bottom of a ladder, you can move up to the top of the ladder.
          3. If you land on the head of a snake, you must slide down to the bottom of the snake.
          4. The first player to get to the FINAL position is the winner.
          5. Hit enter to roll the dice.
          6. Sign up the number of players and names to begin

To make the game more enjoyable limit the number of users to between 1-4

..........................
Snake and ladder positions

snakes_and_ladders = {
    16: 6,
}

1. This part of the code defines a dictionary named snakes_and_ladders 
that maps the positions of snakes and ladders on the game board.
For example, the key-value pair 16: 6 means that if a player lands 
on position 16, they will move to position 6 (climb down a ladder).

2. random.randint function - generates a random integer between 1 and 6
3. The random.randint(1, 6) expression returns a random integer that represents the result of rolling the dice, which is then used to determine how many positions the player should move forward on the board.



