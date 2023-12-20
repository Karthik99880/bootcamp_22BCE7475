import random
from datetime import datetime

a = input("Hello! What is your name?") 
print("Hello "+a+", nice to meet you!")

# Asking how the user is feeling
b = input("How are you feeling today?")

# Adding a loop for a case insensitive match
found_emotion = False
for emotion in ['hungry', 'not feeling well', 'thirsty']:
    if emotion.lower() in b.lower():
        print(f"I see! You should definitely try eating something. Food helps keep us energized and healthy!")
        found_emotion = True
        break

if not found_emotion:
    print("I hope you're having a great day!")

# Asking if the user would like to have a cup of coffee
c = input("Would you like to enjoy a cup of coffee?")

# Adding a loop for a case insensitive match
found_coffee_response = False
for response in ['yes', 'no']:
    if response.lower() in c.lower():
        if 'yes' in response:
            #Usage of random function
            coffee_suggestion = random.choice(["Black", "Espresso", "Cappuccino", "Latte", "Americano"])
            print(f"Excellent choice! Here's your {coffee_suggestion} cup of coffee, and enjoy your day!")
        else:
            print("Of course! If you ever need anything, please don't hesitate to ask!")
        found_coffee_response = True
        break

if not found_coffee_response:
    print("Hmm...I guess we could both use a little boost. Let's go with a 'Just coffee, please' option, shall we?")


d = input("Do you want to watch any movies?")

# Adding a loop for a case insensitive match
found_movie_response = False
for response in ['yes', 'no']:
    if response.lower() in d.lower():
        if 'yes' in response:
            
            current_hour = datetime.datetime.now().hour

            if 5 <= current_hour < 12:
                print("Great! do you want any recommendations on a classic morning movie like Forrest Gump?")
            elif 12 <= current_hour < 17:
                print("Great! do you want any recommendations on a feel-good movie like The Notebook?")
            elif 17 <= current_hour < 21:
                print("Great! do you want any recommendations on a thrilling movie like The Shining?")
            else:
                print("Great! do you want any recommendations on a horror movie like The Conjuring?")
        else:
            print("Okay! There ae a lot of other things which you can do as well.")
        found_movie_response = True
        break

if not found_movie_response:
   print("I'm sorry I couldn't understand your text. Hope you have a great day!")