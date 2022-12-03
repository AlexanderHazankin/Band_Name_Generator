# A small program for a Band Name Generator
from time import sleep

print("Hi there!")
sleep(1)    # Adding delays for extra effects
name = input("What is your name? ")
sleep(1)
print(f"Hello {name}, welcome to the Band Name Generator!👋")
sleep(2)
print("What's name of the city you grew up in?")
city_name = input()
sleep(1)
print("And what's your pet's name?")
pet_name = input()
sleep(1)
print("Hmm")
sleep(1)
print("Let me think...")
count = 0
while count != 5:
    print(".", end="")
    sleep(2 / 5)
    count += 1
print(f"\nI think, your band name could be {city_name} {pet_name}")
