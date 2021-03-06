"""
Edited by: Rowan
Date edited: 15/11/21

Module for generating and checking questions
"""

import random
import win32com.client as wincl

words = {
    "easy": ["apple", "inside", "parents", "guard", "lamb", "wrap", "geese", "gem", "touch", "wreck", "foul",
             "lure", "chief", "bat", "claw", "ship", "raise", "sauce", "leg", "palm", "calm", "weigh", "zeus",
             "row", "zoo", "dead", "city", "door", "tree", "house"],
    "medium": ["training", "flannel", "castle", "quantum", "cancer", "natural", "wizard", "genes", "business",
               "floorboard", "crystal", "sleep", "drawing", "painful", "tasty", "collect", "fake", "slowly", "expand",
               "speedboat", "fries", "brake", "builder", "economy", "dutch", "tunnel", "free", "memory", "mice",
               "music"],
    "hard": ["stitch", "chloroform", "ancient", "switch", "chemotherapy", "artificial", "witch", "chromosomes",
             "commercial", "kitchen", "chrysalis", "conscious", "sketch", "chronic", "delicious", "fetch", "ache",
             "efficient", "stretch", "anchor", "especially", "clutch", "architect", "financial", "hutch", "echo",
             "magician", "memories", "mechanic", "musician"]
}


def question(difficulty):
    return random.choice(words[difficulty]) #returns a random word

def play_audio(word):
    speak = wincl.Dispatch("SAPI.SpVoice") 
    speak.Speak(word) #uses wincl to say the word
