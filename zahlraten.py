import random

number = random.randint(0,101)

guess = int(input("Geben Sie eine Ganzzahl zwischen 1 und 100 ein! "))
if guess > 100 or guess < 0:
    print("***Die eingegebene Zahl ist nicht im Suchbereich enthalten!***")

attempt = 1

while True:
    if guess == number:
        print("Zahl erraten!")
        break
    elif guess <= number:
        print("zu klein")
        attempt += 1
        guess = int(input("Geben Sie eine Ganzzahl zwischen 1 und 100 ein! "))
    elif guess >= number:
        print("zu gross")
        attempt += 1
        guess = int(input("Geben Sie eine Ganzzahl zwischen 1 und 100 ein! "))

print("Sie haben ", attempt, "mal geraten!")
