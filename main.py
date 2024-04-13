# Chatbot
import time
import random
wordList = ["Hi, Nice to meet you.", 'Sup fam.', "Hello!", "Hi! Nice to meet you!"]
busy = [
    'But, I have to assist others.',
    'Sorry, but I have work to do..',
    'We will meet again later. Gtg.',
    'Sorry, but need to go...'
]
Bot = random.choice(wordList)
print(Bot)
Bot2 = str(input("What's your name? > "))
print("Hi " + Bot2 + " You can call me BotMan.")
You = str(input("Say, 'Hi Botman!' > You: "))
print("Sup!")
time.sleep(4)
Bot3 = str(input("Would you like to chat more? > "))
if Bot3 == "No":
    print("Ok, I guess.")
else:
    print(random.choice(busy))
