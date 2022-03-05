import json, os

PHONEBOOK_FILE = "phonebook.json"


def main():
    clear_window()
    intro()

    phonebook = load_phonebook()

    add_person(phonebook)

    save_phonebook(phonebook)


def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')


def intro():
    print("*"*50, "PHONEBOOK 2000", "*"*50)


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