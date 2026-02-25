def madlib(noun, adjective, verb):
    print("The", adjective, noun, "decided", verb, "all day")

madlib("cat","silly", "to dance")

# Modify the function below by adding more layers to make the story your own!
def jungle_adventure():
    # Ask the user to choose between two paths
    path = input("You find two paths: one goes to a river, the other to a mountain. Where do you go? ")

    # Check what the user typed and respond accordingly
    if path == "river":
        print("You can swim with dolphins!")
        choise = input("Would you like to leave, swim or watch?")
        if choise == "leave":
            print("You're leaving")
        elif choise == "swim":
            print("You're swimming with the dolphins!")
        elif choise == "watch":
            print("You're watching the dolphins!")
        else:
            print("A shark will kill you!")
        
    elif path == "mountain":
        print("You can find an ancient temple!")
        choise2 = input("Would you like to leave or find the temple?")
        if choise2 == "leave":
            print("You're leaving")
        elif choise2 == "find the temple":
            print("You found the temple!")
        else:
            print("You will die here without doing nothing!")
        
    else:
        # If the user typed something else, give this outcome
        print("You wander into the jungle and get lost.")

# Start the jungle adventure by calling the function
jungle_adventure()

me = {
 "name": "Daniele",
 "hobby": "using the computer",
 "language": "italian and english",
 "favourite game": "Fortnite",
 "favourite food": "pizza"
    
}
for key, value in me.items():
    print(key, ":", value)

contacts = {
    "Mom": "0000000000",
    "Dad": "0000000000",
    "Grandma": "000000000000"
}
print("Call mom at", contacts["Mom"])

students = [
    {"name": "Sam", "score": 87},
    {"name": "Mary", "score": 65},
    {"name": "Sarah", "score": 50}
]
for student in students:
    print(student['name'], "scored",student['score'])

name = input("What's your name?")
score = input("What's your score?")

with open("scores.txt", "a") as file:
    file.write(name + score + "/n")
    
with open("scores.txt", "r") as file:
    content = name, score
    print(content)

input("Premi INVIO per chiudere")
