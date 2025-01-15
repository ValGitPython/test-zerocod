def print_hello(name):
    print(f"Hello, {name}!")


def user_input_greeting():
    name = input("Enter your name: ")
    print_hello(name)


name=user_input_greeting()
print_hello(name)