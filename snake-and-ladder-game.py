import random

# Constants
BOARD_SIZE = 10
NUM_PLAYERS = 2
FINAL_POSITION = BOARD_SIZE * BOARD_SIZE


# Snakes and Ladders positions
snakes_and_ladders = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

dice_roll = roll_dice()
print(dice_roll)

# # Function to get the position after a dice roll
# def get_position(player, current_position):
#     # Roll the dice
#     dice_roll = roll_dice()
#     # Print the dice roll and current position
#     print(f"Player {player}, you rolled a {dice_roll}. Your current position is {current_position}.")
#     # Calculate the new position after the dice roll
#     new_position = current_position + dice_roll
#     # Check if the new position is a ladder or a snake
#     if new_position in snakes_and_ladders:
#         # Adjust the new position if it's a ladder or a snake
#         new_position = snakes_and_ladders[new_position]
#         # Print a message depending on whether it's a ladder or a snake
#         if new_position > current_position:
#             print(f"You climbed a ladder! You are now at position {new_position}.")
#         else:
#             print(f"Uh oh! You landed on a snake. Slide down to position {new_position}.")
#     # Return the new position
#     return new_position

# # Function to play the game
# def play():
#     print("Welcome to Snake and Ladder Game.")
#     print("Rules:")
#     print("1. Initially all the players are at starting position i.e. 0.")
#     print("2. If you land at the bottom of a ladder, you can move up to the top of the ladder.")
#     print("3. If you land on the head of a snake, you must slide down to the bottom of the snake.")
#     print("4. The first player to get to the FINAL position is the winner.")
#     print("5. Hit enter to roll the dice.")

#     # Player setup
#     players = []
#     for i in range(1, NUM_PLAYERS + 1):
#         player_name = input(f"Enter Player {i}'s name: ")
#         players.append({"name": player_name, "position": 0})

#     # Game loop
#     winner = None
#     while not winner:
#         for i, player in enumerate(players):
#             input(f"{player['name']}, it's your turn. Hit enter to roll the dice.")
#             players[i]["position"] = get_position(player["name"], player["position"])
#             # Check if the player has reached the final position
#             if players[i]["position"] >= FINAL_POSITION:
#                 winner = players[i]["name"]
#                 break

#     # Print the winner
#     print(f"Congratulations, {winner}! You are the winner.")

# # Start the game
# play()
