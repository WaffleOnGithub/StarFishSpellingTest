import win32com.client as wincl

def easyQuestion(easy_word): #gets a random 'easy' word to ask the player
    speakEasy = wincl.Dispatch("SAPI.SpVoice")
    easyW = speakEasy.Speak(easy_word) #says the easy word chosen at the start of the def

def mediumQuestion(medium_word): #gets a random 'medium' word to ask the player
    speakMedium = wincl.Dispatch("SAPI.SpVoice")
    mediumW = speakMedium.Speak(medium_word) #says the medium word chosen at the start of the def

def hardQuestion(hard_word): #gets a random 'hard' word to ask the player
    speakHard = wincl.Dispatch("SAPI.SpVoice")
    hardW = speakHard.Speak(hard_word) #says the hard word chosen at the start of the def


