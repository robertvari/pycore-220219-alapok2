def say_hello(name, age, email=None, address=None):
    print(f"Hello {name}.")
    print(f"You are {age} years old.")

    if email:
        print(f"Your email is {email}.")

    if address:
        print(f"Your address {address}.")


# say_hello("Robert", 32)
# say_hello("Robert", 32, "mail.pythonsuli@gmail.com")
say_hello("Robert", 32, "mail.pythonsuli@gmail.com", "Debrecen")