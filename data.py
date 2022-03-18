import random

bot_data = {
    "name" : "Bot Number {0}".format(random.randint(100,1000)),
    "weather" : random.choice(["rainy", "sunny", "stormy", "warm", "cold"]),
    "mood" : random.choice(["Happy", "Sad", "Depressed", "Cheerful"]),
    "topics": ["Calculus", "Linear Algebra", "Ordinary Differential Equations", "Modern Algebra", "Topology"]
}

openers = ["Hello, what can I help you with?", "Hi, what can I help you with?",
    "Greetings, what can I help you with?", "Hello, how may I help you?", "Hi, how may I help you?",
    "Greetings, how may I help you?", "Good day, how may I help you?"
    ]

keywords = {
    "calculus": ["differentiation", "derivative", "integral", "antidifferentiation," "derivatives", "integrals"],
    "linear algebra": [],
    "differential equations": [],
    "abstract algebra": [],
    "topology" : [],
    "analysis" : []
}

subtopics = {
    "calculus" : ["differential", "integral", "vector", "multivariable"],
    "linear algebra" : ["general","applied"],
    "differential equations" : ["ordinary, partial"],
    "abstract algebra" : ["groups", "rings", "fields", "applications", "galois theory"],
    "topology" : ["manifolds", "algebraic topology", "differential geometry"],
    "analysis" : ["real", "complex"]
}
