import random
from data import bot_data, openers
from responses import reply_manual, reply_moods

class Bot:
    def __init__(self):

        for key in bot_data.keys():
            self.key = bot_data[key]

        self.user_input = input(random.choice(openers) + "\n\n").strip().lower()
        print(self.user_input)
        self.converse()


    def reply_auto(self):
        # This will be the machine learning component of the AI

        self.parse_input()


    def parse_input(self):
        pass


    def converse(self):

        if self.user_input in reply_manual.keys():
            reply = random.choice(reply_manual[self.user_input])

        else:
            reply = self.reply_auto()

        self.user_input = input(reply + "\n\n").strip().lower()
        self.converse()
