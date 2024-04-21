import random

def greet(name):
    greetings = [
        "Hello",
        "Hi",
        "Greetings",
        "Welcome",
        "Hey there"
    ]
    # Randomly select a greeting
    greeting = random.choice(greetings)
    print(f"{greeting}, {name}!")

# Testing the function with "World"
greet("World")