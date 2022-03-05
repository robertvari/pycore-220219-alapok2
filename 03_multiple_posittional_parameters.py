def say_hello(address, name, age, email):
    print(f"Hello {name}.")
    print(f"You are {age} years old.")
    print(f"Your email is {email}.")
    print(f"Your address {address}.")


say_hello("Budapest", "Robert", 32, "robert@gmail.com")
say_hello(
    email="tamas@gmail.com",
    age=23,
    name="Tamás",
    address="Budapest",
)