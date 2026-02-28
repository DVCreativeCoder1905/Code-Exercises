age = 20
if age >= 13:
    print("You can watch movies!")
else:
    print("You're too young to watch movies!")

try:
    numbers = int(input("Enter 2 numbers"))
    print("The half of your numbers is", numbers / 2)
except:
    print("That wasn't a valid number")

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except:
    print("Oops, something went wrong.")

count = 0
while count < 2:
    print("Daniele:", count)
    count = count + 1

# Code for idea 1: Print your name 3 times.
for i in range(3):
    print("Daniele")

# Code for idea 2: Count by 2s.
for i in range(2, 11, 2):
    print(i)

# Code for idea 3: Make a loop that runs until the user types "stop."
text = ""
while text != "stop":
    text = input("Type 'stop' to quit: ")

for i in range(5, 0, -1):
    print(i)
print("Liftoff!")

while True:
    word = input("Write something here:")
    if word == "bye, stop, exit":
        break
    if word == "":
        continue
    print("You typed:", word)

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)

things = ["reading", "coding"]
for thing in things:
    print("One of my favourite things is", thing)

input("Premi INVIO per chiudere")
