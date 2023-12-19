a = input("Hello! What is your name?") 
print("Hello "+a+", nice to meet you!")

b = input("How are you feeling today?")
if('hungry' in b):
    print("I see! You should definitely try eating something. Food helps keep us energized and healthy!")
elif('not feeling well' in b):
    print("I'm really sorry to hear that! I hope you feel better soon!")
    print("Please tell me if I can help you in anyway")
elif('thirsty' in b):
    print("Drinking some water can definitely help quench your thirst!")
else:
    print("I hope you're having a great day!")

print("If you have the time, why not consider having a cup of coffee?")
c = input("Would you like to enjoy a cup of coffee?")
if('yes' in c):
    print("Excellent choice! Here's your cup of coffee, and enjoy your day!")
elif('no' in c):
    print("Of course! If you ever need anything, please don't hesitate to ask!")
else:
    print("If there is anything else I can help,I'd be happy to")

d = input("Do you want to watch any movies")
if('yes' in d):
    print("Great! do you want any recommendations on the go?")
elif('no'in d):
    print("Okay! There ae a lot of other things which you can do as well")
else:
   print("I'm sorry I couldn't understamd you text.Hope you have a great day!")