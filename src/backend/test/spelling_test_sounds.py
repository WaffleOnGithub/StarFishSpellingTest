import win32com.client as wincl
from spelling_test_questions import words

def easyQuestion(easy_word):
    speakEasy = wincl.Dispatch("SAPI.SpVoice")
    easyW = speakEasy.Speak(easy_word)

def mediumQuestion(medium_word):
    speakMedium = wincl.Dispatch("SAPI.SpVoice")
    mediumW = speakMedium.Speak(medium_word)

def hardQuestion(hard_word):
    speakHard = wincl.Dispatch("SAPI.SpVoice")
    hardW = speakHard.Speak(hard_word)


