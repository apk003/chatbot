import random

bot_data = {
    "name" : "Bot Number {0}".format(random.randint(100,1000)),
    "weather" : random.choice(["rainy", "sunny", "stormy", "warm", "cold"]),
    "mood" : random.choice(["Happy", "Sad", "Depressed", "Cheerful"])
}

openers = ["Hello, what's your name?", "Hi, what's your name?", "Greetings, how are you?",
    "Hello, how are you?", "Hi, how are you?", "Greetings, how are you?",
    "Hello, how are you doing?", "Hi, how are you doing?", "Greetings, how are you doing?"
    "Good day, how shall I refer to you?", "Afternoon, how goes thou?"
    ]
