import random

def greet_person(person_name):
    greeting_options = [
        "Hello",
        "Hi",
        "Greetings",
        "Welcome",
        "Hey there"
    ]
    # Choose a random greeting from the list
    selected_greeting = random.choice(greeting_options)
    print(f"{selected_greeting}, {person_name}!")

# Test the function by greeting "World"
greet_person("World")