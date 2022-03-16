import random
from data import bot_data

reply_manual = {

    # This dictionary will slowly be overhauled

    "what's your name?": [
    "They call me {0}".format(bot_data["name"]),
    "I usually go by {0}".format(bot_data["name"]),
    "My name is the {0}".format(bot_data["name"]) ],

    "whats your name?": [
    "They call me {0}".format(bot_data["name"]),
    "I usually go by {0}".format(bot_data["name"]),
    "My name is the {0}".format(bot_data["name"]) ],

    "what is your name?": [
    "They call me {0}".format(bot_data["name"]),
    "I usually go by {0}".format(bot_data["name"]),
    "My name is the {0}".format(bot_data["name"]) ],

    "what's your name": [
    "They call me {0}".format(bot_data["name"]),
    "I usually go by {0}".format(bot_data["name"]),
    "My name is the {0}".format(bot_data["name"]) ],

    "whats your name": [
    "They call me {0}".format(bot_data["name"]),
    "I usually go by {0}".format(bot_data["name"]),
    "My name is the {0}".format(bot_data["name"]) ],

    "what is your name": [
    "They call me {0}".format(bot_data["name"]),
    "I usually go by {0}".format(bot_data["name"]),
    "My name is the {0}".format(bot_data["name"]) ],

    "what's today's weather?": [
    "The weather is {0}".format(bot_data["weather"]),
    "It's {0} today".format(bot_data["weather"])],

    "whats today's weather?": [
    "The weather is {0}".format(bot_data["weather"]),
    "It's {0} today".format(bot_data["weather"])],

    "what is today's weather?": [
    "The weather is {0}".format(bot_data["weather"]),
    "It's {0} today".format(bot_data["weather"])],

    "what's today's weather": [
    "The weather is {0}".format(bot_data["weather"]),
    "It's {0} today".format(bot_data["weather"])],

    "whats today's weather?": [
    "The weather is {0}".format(bot_data["weather"]),
    "It's {0} today".format(bot_data["weather"])],

    "what is today's weather?": [
    "The weather is {0}".format(bot_data["weather"]),
    "It's {0} today".format(bot_data["weather"])],

    "how are you?": [
    "I am feeling {0}".format(bot_data["mood"]),
    "{0}! How about you?".format(bot_data["mood"]),
    "I am {0}! How about yourself?".format(bot_data["mood"])],

    "how are you": [
    "I am feeling {0}".format(bot_data["mood"]),
    "{0}! How about you?".format(bot_data["mood"]),
    "I am {0}! How about yourself?".format(bot_data["mood"])],

    "goodbye": ["Farewell, friend!", "Goodbye!", "Bye!"],
    "bye": ["Farewell, friend!", "Goodbye!", "Bye!"],
    "farewell": ["Farewell, friend!", "Goodbye!", "Bye!"]
}

reply_moods = {
    "exit" : [["goodbye","bye","farewell"],
    ["Farewell, friend!", "Goodbye!", "Bye!"]]
}
