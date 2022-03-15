import random
from data import bot_data

class bot:
    def __init__(self):

        for key in bot_data.keys():
            self.key = bot_data[key]
