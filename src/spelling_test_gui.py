"""
Edited by: Joe
Date edited: 22/11/21

Main GUI that calls on custom subroutines to have a working spelling test
TODO: leaderbboard frame, set authorised to false for later, implement other modules
"""
from tkinter import* #imports tkinter
import tkinter as tk
from tkinter import ttk #imports ttk for imporved widget styling
from tkinter import messagebox
import backend #imports custom backend code

def splash_screen(): #function to display the initial frame
    button = ttk.Button(splash_screen_frame, text="sign up", command=signup) #creates a button
    button.grid(row=0,column=0,sticky="W") #positions the button on a grid
    button1 = ttk.Button(splash_screen_frame, text="sign in", command=signin)
    button1.grid(row=0,column=1,sticky="W")
    splash_screen_frame.pack() #makes the frame visible
    
def signup(): #function to display the signup frame
    global current_frame #imports the global variable used for navigating between frames
    current_frame = "signup_frame" #sets the current_frame to the current frame
    text1 = ttk.Label(signup_frame,text="Enter your username: ") #creates a label widget
    text1.grid(row=0,column=0,sticky="W") #places it on the grid
    text2 = ttk.Label(signup_frame,text="Enter your password: ")
    text2.grid(row=1,column=0,sticky="W")
    text3 = ttk.Label(signup_frame,text="Enter your email: ")
    text3.grid(row=2,column=0,sticky="W")
    
    textbox = ttk.Entry(signup_frame, textvariable=username) #creates an entry widget for the user to enter text
    textbox.grid(row=0,column=1,sticky="W") #places the entry widget on a grid
    textbox1 = ttk.Entry(signup_frame, textvariable=password)
    textbox1.grid(row=1,column=1,sticky="W")
    textbox2 = ttk.Entry(signup_frame, textvariable=email)
    textbox2.grid(row=2,column=1,sticky="W")

    button3 = ttk.Button(signup_frame,text="back",command=back) #goes back to the previous frame
    button3.grid(row=3,column=0,sticky="W")
    button4 = ttk.Button(signup_frame,text="submit",command=signup_button) #runs a procedure that adds the information to the database
    button4.grid(row=3,column=1,sticky="W")

    splash_screen_frame.pack_forget() #makes the splash frame invisible
    signup_frame.pack() #displays the sign up frame 
    
def signin(): #function to display the sign in frame
    global current_frame
    current_frame = "signin_frame"
    text4 = ttk.Label(signin_frame,text="Enter your username: ")
    text4.grid(row=0,column=0,sticky="W")
    text5 = ttk.Label(signin_frame,text="Enter your password: ")
    text5.grid(row=1,column=0,sticky="W")
    text6 = ttk.Label(signin_frame,text="Enter your email: ")
    text6.grid(row=2,column=0,sticky="W")

    textbox3 = ttk.Entry(signin_frame, textvariable=username)
    textbox3.grid(row=0,column=1,sticky="W")
    textbox4 = ttk.Entry(signin_frame, textvariable=password)
    textbox4.grid(row=1,column=1,sticky="W")
    textbox5 = ttk.Entry(signin_frame,textvariable=email)
    textbox5.grid(row=2,column=1,sticky="W")
    
    button3 = ttk.Button(signin_frame,text="back",command=back)
    button3.grid(row=3,column=0,sticky="W")
    button4 = ttk.Button(signin_frame,text="submit",command=signin_button) #verifies the users information
    button4.grid(row=3,column=1,sticky="W")
    
    splash_screen_frame.pack_forget()
    signin_frame.pack()
def two_step(): #function to display the two step verification frame 
    global current_frame
    current_frame="two_step_frame"
    text7 = ttk.Label(two_step_frame,text="Please enter the code sent to your email adress: ")
    text7.grid(row=0,column=0,sticky="W")

    textbox6 = ttk.Entry(two_step_frame,textvariable=auth_code)
    textbox6.grid(row=0,column=1,sticky="W")

    button5 = ttk.Button(two_step_frame,text="back",command=back)
    button5.grid(row=3,column=0,sticky="W")
    button6 = ttk.Button(two_step_frame,text="submit",command=two_step_auth_button) #function that will check the users input against the code sent by the code
    button6.grid(row=3,column=1,sticky="W")
    
    signin_frame.pack_forget()
    two_step_frame.pack()
def dificulty_select(): #frame that displays the dificulty select frame
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
def test(dificulty): #function that displays the actual spelling test frame, the dificulty is passed as a parameter
    global current_frame
    current_frame="test"
    text9 = ttk.Label(test_frame,text="Spell what you hear! use the return key to submit")
    text9.grid(row=0,column=0,columnspan=2)

    button11 = ttk.Button(test_frame,text="Play Audio",command=play_audio)
    button11.grid(row=2,column=1)
    button12 = ttk.Button(test_frame,text="Leaderboard",command=leaderboard)
    button12.grid(row=2,column=0)
    
    textbox7 = ttk.Entry(test_frame, textvariable=word)
    textbox7.grid(row=1,column=0,columnspan=2)

    dificulty_select_frame.pack_forget()
    test_frame.pack()
def leaderboard(): #function that displays the leaderboard at the end of the game
    test_frame.pack_forget()
    text9 = ttk.Label(leaderboard_frame,text="Top 5 users:")
    text9.grid(row=0,column=0)
    leaderboard_frame.pack()
    
def signup_button(): #function that runs when the sign up button is clicked
    signup_frame.pack_forget()
    splash_screen()
    
def signin_button(): #function that runs when the sign in button is clicked to check if the user has successfully logged in
    global authorised
    if authorised == True:
        signin_frame.pack_forget()
        two_step()
    else:
        messagebox.showerror('error', 'Login details incorrect')
    
def two_step_auth_button(): #function that runs when the two step verification code is submitted
    big_test = backend.send_email("buckleypad@gmail.com")
    print(big_test)
    global twoauthorised
    if twoauthorised == True:
        dificulty_select()
    else:
        messagebox.showerror('error', '2 step authorization code incorrect')
def easy_button(): #function that runs the test on easy dificulty
    test("easy")
    
def medium_button(): #function that runs the test on medium dificulty
    test("medium")
    
def hard_button(): #function that runs the test on hard dificulty
    test("hard")
    
def back(): #code that runs when the back button is pressed
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
    else:
        print("How?")
def play_audio(): #code that plays the correct audio file in the spelling test
    #code to select and play the audio file
    print()
def submit_answer(self):#code that submits the answer to be checked
    global current_frame
    if current_frame == "test":
        answer = word.get()
        print(answer)
    else:
        pass
    
root = tk.Tk() #gives the container the identifier "root"
root.title("Spelling test") #gives the window title
root.bind('<Return>', submit_answer)

splash_screen_frame = ttk.Frame(root) #creates a new frame that widgets can be added to independently of other frames
signup_frame = ttk.Frame(root)
signin_frame = ttk.Frame(root)
two_step_frame = ttk.Frame(root)
dificulty_select_frame = ttk.Frame(root)
test_frame = ttk.Frame(root)
leaderboard_frame = ttk.Frame(root)

global current_frame,authorised,twoauthorised  #creates global variables used to navigate between frames
authorised = True #will be turned true when the user has succesfully logged in and is allowed to use the program
twoauthorised = True

username = tk.StringVar() #empty string variable that will hold the users username when submitted
password = tk.StringVar() #empty string that will hold the uers password when submitted
email = tk.StringVar() #empty string that will hold the uers email when submitted
auth_code = tk.StringVar() #empty string that will hold the users 2 step autherisation code when submitted
word = tk.StringVar()

splash_screen() #displays the splash screen

root.mainloop() #runs the graphical code infinitly and is only interupted by mouse clicks
