import random

greetings = ["hola", "hello", "hi", "Hi", "hey!", "hey"]
greeting_responses = ["Hi, I'm a robot", "What's up, I'm bob"]

question = ["How are you?", "How are you doing?"]
question_responses = ["Okay", "I'm fine"]


while True:
    userInput = input("Type something! >>> ")
    if userInput in greetings:
        random_greeting = random.choice(greeting_responses)
        print(random_greeting)
    elif userInput in question:
        random_response = random.choice(question_responses)
        print(random_response)
    else:
        print("I did not understand what you said")

