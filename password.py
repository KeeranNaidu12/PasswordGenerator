import random
# Import the module
from tkinter import *

#booleans
lengthDone = False

# Building the root window
base = Tk()

# Save the length of the password
length = IntVar()
caps = IntVar()
special = IntVar()
numbers = IntVar()

# Window title and Dimensions
base.title("Python Password Generator")
base.geometry('400x350')

prompt = Label(base,text = "Welcome to my randomized password generator")
prompt.grid(row=1,column=0)

note = Label(base,text = "NOTE: Your password CANNOT exceed 20 characters")
note.grid(row=3,column=0)

def startClicked():
    prompt.configure(text = "How many characters would you like your password to be?")
    

clicker = Button(base,text = "Click here", command = startClicked)
clicker.grid()



base.mainloop()

def yesCheck(option):
    if (option.lower() == "no"):
        return False
    else:
        return True


#---------START-OF-PROGRAM---------------------------------------------------------------------------

password = ""


print("Got it! Your password will be ", value ," characters long.")

# Special Characters?
print("Would you like to have special characters (like *,+,!, etc.) in your password? (Yes/No)")
option1 = input()

if(yesCheck(option1) == True):
    print("We will consider this!")
else: 
    print("We will not consider this!")

# Numbers?
print("Would you like to have numbers in your password? (Yes/No)")
option2 = input()

if(yesCheck(option2) == True):
    print("We will consider this!")
else: 
    print("We will not consider this!")

# Captial Letters?
print("Would you like to have capital letters in your password? (Yes/No)")
option3 = input()

if(yesCheck(option3) == True):
    print("We will consider this!")
else: 
    print("We will not consider this!")

# Building the password using these conditions
counter = 0
while counter < value:
    choice = random.randint(1,4)

    if option1.lower() == "yes" and choice == 1:
        password += chr(random.randint(33,47))   
    elif option2 == "yes" and choice == 2:
        password += chr(random.randint(48,57))
    elif option3 == "yes" and choice == 3:
        password += chr(random.randint(65,90))
    else:
        password += chr(random.randint(97,122))
        
    counter+=1

print(password)
