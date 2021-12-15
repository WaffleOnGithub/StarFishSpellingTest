"""
Last edited by: Joe
Date edited: 15/12/21

Main GUI that calls on custom subroutines to have a working spelling test
TODO: leaderboard frame,fix formatting on the signup/signin error boxes
known bugs:
"""
from tkinter import*
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import backend 

def splash_screen():
    """
    function that creates the landing frame's graphics
    """
    button = ttk.Button(splash_screen_frame, text="sign up", command=signup) 
    button.grid(row=0,column=0,sticky="W") 
    button1 = ttk.Button(splash_screen_frame, text="sign in", command=signin)
    button1.grid(row=0,column=1,sticky="W")
    splash_screen_frame.pack()
    
def signup():
    """
    function that creates the signup frames's graphics
    """
    global current_frame
    current_frame = "signup_frame"
    #sets the current frame for navigation between frames
    text1 = ttk.Label(signup_frame,text="Enter your username: ")
    #creates a widget
    text1.grid(row=0,column=0,sticky="W")
    #places it on the grid
    text2 = ttk.Label(signup_frame,text="Enter your password: ")
    text2.grid(row=1,column=0,sticky="W")
    text3 = ttk.Label(signup_frame,text="Enter your email: ")
    text3.grid(row=2,column=0,sticky="W")
    
    textbox = ttk.Entry(signup_frame, textvariable=username) 
    textbox.grid(row=0,column=1,sticky="W") 
    textbox1 = ttk.Entry(signup_frame, textvariable=password)
    textbox1.grid(row=1,column=1,sticky="W")
    textbox2 = ttk.Entry(signup_frame, textvariable=email)
    textbox2.grid(row=2,column=1,sticky="W")

    button3 = ttk.Button(signup_frame,text="back",command=back)
    button3.grid(row=3,column=0,sticky="W")
    button4 = ttk.Button(signup_frame,text="submit",command=signup_button)
    button4.grid(row=3,column=1,sticky="W")

    splash_screen_frame.pack_forget() #makes the splash frame invisible
    signup_frame.pack() #displays the sign up frame 
    
def signin():
    """
    function that creates the signin frames's graphics
    """
    global current_frame
    current_frame = "signin_frame"
    text4 = ttk.Label(signin_frame,text="Enter your username: ")
    text4.grid(row=0,column=0,sticky="W")
    text5 = ttk.Label(signin_frame,text="Enter your password: ")
    text5.grid(row=1,column=0,sticky="W")
    text6 = ttk.Label(signin_frame,text="Enter your Email: ")
    text6.grid(row=2,column=0,sticky="W")

    textbox3 = ttk.Entry(signin_frame, textvariable=username)
    textbox3.grid(row=0,column=1,sticky="W")
    textbox4 = ttk.Entry(signin_frame, textvariable=password)
    textbox4.grid(row=1,column=1,sticky="W")
    textbox5 = ttk.Entry(signin_frame, textvariable=email)
    textbox5.grid(row=2,column=1,sticky="W")

    button3 = ttk.Button(signin_frame,text="back",command=back)
    button3.grid(row=3,column=0,sticky="W")
    button4 = ttk.Button(signin_frame,text="submit",command=signin_button) 
    button4.grid(row=3,column=1,sticky="W")
    
    splash_screen_frame.pack_forget()
    signin_frame.pack()
def two_step():
    """
    function that creates the two step verification frames's graphics and sends an email to the specified email adress
    """
    global current_frame,passcode
    passcode = backend.send_email(email.get())
    current_frame="two_step_frame"
    text7 = ttk.Label(two_step_frame,text="Please enter the code sent to your email adress: ")
    text7.grid(row=0,column=0,sticky="W")

    textbox6 = ttk.Entry(two_step_frame,textvariable=auth_code)
    textbox6.grid(row=0,column=1,sticky="W")

    button5 = ttk.Button(two_step_frame,text="back",command=back)
    button5.grid(row=3,column=0,sticky="W")
    button6 = ttk.Button(two_step_frame,text="submit",command=two_step_auth_button)
    button6.grid(row=3,column=1,sticky="W")
    
    signin_frame.pack_forget()
    two_step_frame.pack()
def dificulty_select():
    """
    function that creates the two dificulty select frames's graphics
    """
    global current_frame
    current_frame="dificulty_select_frame"
    text8 = ttk.Label(dificulty_select_frame,text="Please select your dificulty:")
    text8.grid(row=0,column=0,sticky="W")

    button7 = ttk.Button(dificulty_select_frame,text="Easy",command=easy_button)
    button7.grid(row=1,column=0)
    button8 = ttk.Button(dificulty_select_frame,text="Medium",command=medium_button)
    button8.grid(row=2,column=0)
    button9 = ttk.Button(dificulty_select_frame,text="Hard",command=hard_button)
    button9.grid(row=3,column=0)
    button10 = ttk.Button(dificulty_select_frame,text="Back",command=back)
    button10.grid(row=4,column=0)
    
    two_step_frame.pack_forget()
    dificulty_select_frame.pack()
def test(difficulty):
    """
    function that creates the two step test frames's graphics and passes the users selected dificulty as a parameter
    """
    global current_frame
    current_frame="test"
    text9 = ttk.Label(test_frame,text="dificulty: "+difficulty)
    text9.grid(row=0,column=0,columnspan=2,sticky="W")
    text10 = ttk.Label(test_frame,text="Score: "+str(score))
    text10.grid(row=0,column=2,sticky="W")

    textbox7 = ttk.Entry(test_frame, textvariable=user_word)
    textbox7.grid(row=1,column=0,columnspan=2,sticky="W")

    button11 = ttk.Button(test_frame,text="Leaderboard",command=leaderboard)
    button11.grid(row=2,column=1)
    button12 = ttk.Button(test_frame,text="Next Word",command=lambda: play_audio(difficulty))
    button12.grid(row=2,column=2)
    button13 = ttk.Button(test_frame,text="Submit",command=lambda: submit_answer(user_word.get()))
    button13.grid(row=1,column=2)
    button13 = ttk.Button(test_frame,text="Back",command=back)
    button13.grid(row=2,column=0)

    dificulty_select_frame.pack_forget()
    test_frame.pack()
def leaderboard():
    """
    function that displays the leaderboard at the end of the game
    """
    backend.save_data(username, score)
    test_frame.pack_forget()
    text9 = ttk.Label(leaderboard_frame,text="Top 5 users:")
    text9.grid(row=0,column=0)

    leaderboard_frame.pack()
    
def signup_button():
    """
    function that erases the previous frame, adds the users details to a database and then prompts the uesr to sign in if the data was saved correctly
    """
    if username.get()== "":
       messagebox.showerror('Input fields cannot be left blank')
    elif  password.get() =="":
       messagebox.showerror('Input fields cannot be left blank')
    elif email.get() =="":
       messagebox.showerror('Input fields cannot be left blank')
    else:
        auth = backend.register(username.get(), password.get(), email.get())
        print(auth)
        signup_frame.pack_forget()
        splash_screen()
    
def signin_button(): 
    """
    function that checks the users credentials against the database and moves forward if correct
    """
    if username.get()== "":
       messagebox.showerror('Input fields cannot be left blank')
    elif  password.get() =="":
       messagebox.showerror('Input fields cannot be left blank')
    elif email.get() =="":
        messagebox.showerror('Input fields cannot be left blank')
    else:
        #uses the users inputs as parameters for login
        auth = backend.login(username.get(), password.get())["success"]
        if auth == True:
            signin_frame.pack_forget()
            two_step()
        else:
                   messagebox.showerror('Login details incorrect')

    signup_frame.pack_forget()
    two_step
    
def two_step_auth_button():
    """
    function that checks the users credentials against the database and moves forward if correct
    """    
    if  passcode == auth_code.get():
        dificulty_select()
    else:
       messagebox.showerror('error', '2 step authorization code incorrect')
        
def easy_button():
    """
    function that runs the test code passing "easy" as a parameter
    """
    test("easy")
    
def medium_button():
    """
    function that runs the test code passing "medium" as a parameter
    """
    test("medium")
    
def hard_button():
    """
    function that runs the test code passing "hard" as a parameter
    """
    test("hard")
    
def back():
    """
    function that chekcs the current frame and sends the user back a frame
    """
    global current_frame
    if current_frame == "signup_frame": 
        signup_frame.pack_forget()
        splash_screen()
    elif current_frame == "signin_frame":
        signin_frame.pack_forget()
        splash_screen()
    elif current_frame == "two_step_frame":
        two_step_frame.pack_forget()
        signin()
    elif current_frame == "dificulty_select_frame":
        dificulty_select_frame.pack_forget()
        two_step()
    elif current_frame == "test":
        test_frame.pack_forget()
        dificulty_select()
    else:
        print("How?")
        
def play_audio(difficulty):
    """
    function that picks a word and plays the appropiate audio
    the "run" variable is used to work around the fact python automatically runs any functions that have parameters passed to them
    """
    global word
    word = backend.question(difficulty)
    print(word)
    if word in used_words == True:
        play_audio(difficulty) #runs the function again
    else:
        used_words.append(word) #adds the word to an array so it can't be reused
        backend.play_audio(word)

def submit_answer(user_word):
    """
    function that reads the users input, checks against the selected word and updates scores
    """
    print("call")
    global score,word
    answer = user_word
    if answer == word:
        print(score)
        score= score+1
        print(score)
        text10 = ttk.Label(test_frame,text="Score: "+str(score))
        text10.grid(row=0,column=2,sticky="W")
        
    else:
        print("incorrect")
        pass
    
root = tk.Tk()
root.title("Spelling test")
root.bind('<Return>', submit_answer) #allows the uesr to press the return key to submit their answer(this runs the function correctly unlike the submit button)

""""
creating different frames to be used by the program
"""""
splash_screen_frame = ttk.Frame(root)
signup_frame = ttk.Frame(root)
signin_frame = ttk.Frame(root)
two_step_frame = ttk.Frame(root)
dificulty_select_frame = ttk.Frame(root)
test_frame = ttk.Frame(root)
leaderboard_frame = ttk.Frame(root)

""""
declaring global vairables and asigning default values
"""""
global current_frame,authorised,passcode,word,score,used_words
score = 0
word = ""
used_words = []
run = False
run2 = False
authorised = True
twoauthorised = True

""""
defining variables to be used by input fields in the program
"""""
username = tk.StringVar()
password = tk.StringVar() 
email = tk.StringVar() 
auth_code = tk.StringVar() 
user_word = tk.StringVar()

dificulty_select()
#runs the first function that starts the program
root.mainloop()