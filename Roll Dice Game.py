import random


def roll_die():
    """Roll a six-sided die and return the result."""
    return random.randint(1, 6)


def play():
    print("Welcome to the Dice Roll Game!")

    while True:
        input("Press Enter to roll the dice...")
        player_roll = roll_die()
        computer_roll = roll_die()

        print(f"You rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")

        if player_roll > computer_roll:
            print("You win!")
        elif player_roll < computer_roll:
            print("Computer wins!")
        else:
            print("It's a tie!")

        play_again = input("Roll again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play()
