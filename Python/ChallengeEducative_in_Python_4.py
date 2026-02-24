def chatbot():
    print("Hi! I'm ChatPy. Let's chat. Type 'bye' to exit.")

    while True:
        msg = input("You: ")

        if msg == "bye":
            print("ChatPy: See you later!")
            break
        elif msg == "I like music":
            print("ChatPy: Amazing!")
        elif msg == "Hello":
            print("ChatPy: Hi, I'm ChatPy, your Python chatbot")
        else:
            print("ChatPy: You said:", msg)

chatbot()

import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
die = die1 + die2
print("We rolled a", die)

input("Premi INVIO per chiudere")