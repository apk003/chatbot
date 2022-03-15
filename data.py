import random

bot_data = {
    "name" : "Bot Number {0}".format(random.randint(100,1000)),
    "weather" : random.choice(["rainy", "sunny", "stormy", "warm", "cold"]),
    "mood" : random.choice(["Happy", "Sad", "Depressed", "Cheerful"])
}
