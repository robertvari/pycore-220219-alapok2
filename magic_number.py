import random

min_number = 0
max_number = 10
max_tries = 3


def main():
    # print some intro about the game
    intro()

    # get a random number: import random, random.randint(a, b)
    magic_number = random.randint(min_number, max_number)
    print(f"DEBUG: {magic_number}")

    # get player number
    player_guess = get_player_number()

    # check player number
    player_guess = check_numbers(magic_number, player_guess)

    # print game result
    print_game_result(magic_number, player_guess)

    # ask player if he/she wants to play again
    play_again = input("Do you want to play again? (y/n)")
    if play_again == "y":
        main()
    else:
        print("See you later!")


def intro():
    print("*"*50, "MAGIC NUMBERS", "*"*50)
    print(f"There is number between {min_number} and {max_number}. Can you guess it?")
    print(f"You have {max_tries} tries.")


def get_player_number():
    player_number = input("Your guess:")

    # todo check player_number

    return player_number


def check_numbers(magic_number, player_number):
    _max_tries = max_tries

    # if player_number == magic_number returns player_number
    while player_number != str(magic_number):
        _max_tries -= 1

        if _max_tries == 0:
            print("You have no more tries :(")
            print("Maybe next time!")
            break

        print(f"Wrong number :( You have {_max_tries} tries left.")
        player_number = get_player_number()

    return player_number


def print_game_result(magic_number, player_number):
    if player_number == str(magic_number):
        print(f"You win!!! My number was {magic_number}")
    else:
        print(f"Game over... My number was {magic_number}")


main()
