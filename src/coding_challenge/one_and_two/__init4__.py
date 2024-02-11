ROCK_PAPER_SCISSORS = ["rock", "paper", "scissors"]
from random import randint

def rps_win_or_lost(player_choice: str) -> bool:
    """Checks if player's hand wins or loses.
    
    Depending on whether 'rock', 'paper', or 'scissors' is passed - check if
    the user beats the computer.
    
    :param player_choice: The player's choice ('rock', 'paper', or 'scissors').
    :return: True if the player wins, False if the player loses or it's a tie.
    """

    def get_cpu_tactic() -> str:
        """Generates the computer's move.
        
        Uses the random package's randint() to select a tactic's index from
        ROCK_PAPER_SCISSORS.
        
        :return string: member of ROCK_PAPER_SCISSORS
        """
        return ROCK_PAPER_SCISSORS[randint(0, 2)]

    cpu_choice = get_cpu_tactic()

    # victory condition
    if player_choice == cpu_choice:
        print(f"tie {player_choice}.")
        return False
    elif (
        (player_choice == "rock" and cpu_choice == "scissors") or
        (player_choice == "paper" and cpu_choice == "rock") or
        (player_choice == "scissors" and cpu_choice == "paper")
    ):
        print(f"A winner is you! {player_choice} beats {cpu_choice}.")
        return True
    else:
        print(f"get rekt nerd, {cpu_choice} beats {player_choice}.")
        return False

# function test
def main():
    attempts = 0

    while attempts < 3:  # Adjusted condition for the loop // I would have preferred the initial stages not actually counting towards valid attempts
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if player_choice in ROCK_PAPER_SCISSORS:
            result = rps_win_or_lost(player_choice)
        else:
            if attempts == 0:
                print("Can you not read? Please choose rock, paper, or scissors.")
            else:
                print("Seriously? It's not that difficult. Choose rock, paper, or scissors.")

            attempts += 1
            continue  # Continue to the next iteration without checking the result

        if result:
            break  # Exit the loop if the choice is valid and the user wins

        attempts += 1

    if attempts == 3:  # Adjusted condition for exiting the program
        print("You seem to have trouble with this. Exiting the game.")

if __name__ == "__main__":
    main()
