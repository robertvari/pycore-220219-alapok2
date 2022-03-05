import json, os

PHONEBOOK_FILE = "phonebook.json"


def main():
    clear_window()
    intro()

    phonebook = load_phonebook()

    user_choice = input()

    if user_choice == "3":
        exit()
    elif user_choice == "1":
        # todo nice print
        print(phonebook)
        input("Press enter to continue...")
        main()
    elif user_choice == "2":
        add_person(phonebook)
        save_phonebook(phonebook)
        input("Press enter to continue...")
        main()
    else:
        print("I don't understand :(")
        exit()


def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')


def intro():
    print("*"*50, "PHONEBOOK 2000", "*"*50)
    print("1. Print phonebook\n2. Add person\n3. Exit program")


def load_phonebook():
    phonebook = {}

    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE) as f:
            phonebook = json.load(f)

    return phonebook


def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, "w") as f:
        json.dump(phonebook, f)

    print("Phonebook saved.")


def add_person(phonebook):
    name = input("What is your name?")
    email = input("Email?")
    phone = input("Phone?")
    address = input("Address?")

    phonebook[phone] = {
        "name": name,
        "address": address,
        "email": email
    }


main()