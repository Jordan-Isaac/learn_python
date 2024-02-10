#ChatGPT optimised
ROCK_PAPER_SCISSORS = ["rock", "paper", "scissors"]
ATTEMPT_LIMIT = 3

def rps_win_or_lost(player_choice: str) -> bool:
    """Checks if the player's hand wins or loses."""
    def get_cpu_tactic() -> str:
        """Generates the computer's move."""
        return ROCK_PAPER_SCISSORS[randint(0, 2)]

    cpu_choice = get_cpu_tactic()

    # Victory condition
    if player_choice == cpu_choice:
        print(f"Tie! {player_choice}.")
        return False
    elif (
        (player_choice == "rock" and cpu_choice == "scissors") or
        (player_choice == "paper" and cpu_choice == "rock") or
        (player_choice == "scissors" and cpu_choice == "paper")
    ):
        print(f"A winner is you! {player_choice} beats {cpu_choice}.")
        return True
    else:
        print(f"Get rekt nerd! {cpu_choice} beats {player_choice}.")
        return False

def main():
    attempts = 0

    while attempts < ATTEMPT_LIMIT:
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

    if attempts == ATTEMPT_LIMIT:
        print("You seem to have trouble with this. Exiting the game.")

if __name__ == "__main__":
    main()