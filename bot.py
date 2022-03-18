import random
from data import bot_data, openers, keywords
from responses import reply_general, reply_moods

class Bot:
    def __init__(self):

        self.name = bot_data["name"]
        self.mood = bot_data["mood"]
        self.weather = bot_data["weather"]
        self.topics = bot_data["topics"]

        self.user_input = input(random.choice(openers) + " I am {0}.\n\n".format(self.name)).strip().lower()
        self.converse()


    def reply_auto(self):
        # This will be the machine learning component of the AI

        self.parse_input()


    def parse_input(self):
        sentence = self.user_input.split()

        # Note that this only finds the first keyword for now
        for word in sentence:
            for topic in keywords:
                if word in topic:
                    return [word,topic]


    def converse(self):

        if self.user_input in reply_general.keys():
            reply = random.choice(reply_general[self.user_input])

        else:
            reply = "You would like help with " + self.parse_input()[0] + "?"

        self.user_input = input(reply + "\n\n").strip().lower()
        self.converse()
