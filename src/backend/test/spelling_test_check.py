import random

difficulties = {
    "easy": ["apple", "inside", "parents", "guard", "lamb", "wrap", "geese", "gem", "touch", "wreck", "foul",
             "lure", "chief", "bat", "claw", "ship", "raise", "sauce", "leg", "palm", "calm", "weigh", "zeus",
             "row", "zoo", "dead", "city", "door", "tree", "house"],
    "medium": ["training", "sulfer", "castle", "quantum", "cancer", "natural", "wizard", "genes", "business",
               "floorboard", "crystal", "sleep", "drawing", "painful", "tasty", "collect", "fake", "slowly", "expand",
               "speedboat", "fries", "brake", "builder", "economy", "dutch", "tunnel", "free", "memory", "mice", "music"],
    "hard": ["stitch", "chloroform", "ancient", "switch", "chemotherapy", "artificial", "witch", "chromosomes",
             "commercial", "kitchen", "chrysalis", "conscious","sketch", "chronic", "delicious", "fetch", "ache",
             "efficient", "stretch", "anchor", "especially", "clutch", "architect", "financial", "hutch", "echo",
             "magician", "memories", "mechanic", "musician"]
}


def question(difficulty):
    return random.choice(difficulties[difficulty])


def check(answer, correct):
    return correct == answer
