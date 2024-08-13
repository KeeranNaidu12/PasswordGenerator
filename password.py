import random
# Import the module
import tkinter as tk

# Building the root window
base = tk.Tk()

# Save the length of the password
lowerNo = tk.IntVar()
capsNo = tk.IntVar()
specialNo = tk.IntVar()
numbersNo = tk.IntVar()

lower = lowerNo.get()
caps = capsNo.get()
special = specialNo.get()
numbers = numbersNo.get()
sum = 0

# Window title and Dimensions
base.title("Python Password Generator")
base.geometry("650x1600")





welcome = tk.Label(base,text = "Welcome to my randomized password generator!", font=('arial',20,'bold'))
welcome.grid(row=1,column=1, sticky= tk.N,pady=20, padx=80)

note = tk.Label(base,text = "NOTE: Your password CANNOT exceed 20 characters", font=('arial',15,'bold'))
note.grid(row=2,column=1,ipadx=30, ipady=10)

prompt = tk.Label(base,text = "Specify how many characters you want for each category!")
prompt.grid(row=20,column=1, pady=30)

#These are the different Entries
option1L = tk.Label(base,text = "LowerCases")
option1L.grid(row=30,column=1, pady=10,sticky=tk.W, padx= 200)

option1E = tk.Entry(base,textvariable = lowerNo, font=('arial',10))
option1E.grid(row=30,column=1, pady=10, sticky=tk.W, padx = 300)

option1L = tk.Label(base,text = "Captials")
option1L.grid(row=40,column=1, pady=10,sticky=tk.W, padx= 200)

option1E = tk.Entry(base,textvariable = capsNo, font=('arial',10))
option1E.grid(row=40,column=1, sticky=tk.W,pady=10, padx = 300)

option1L = tk.Label(base,text = "Numbers")
option1L.grid(row=50,column=1, pady=10,sticky=tk.W, padx= 200)

option1E = tk.Entry(base,textvariable = numbersNo, font=('arial',10))
option1E.grid(row=50,column=1, sticky=tk.W,padx = 300, pady=10)

option1L = tk.Label(base,text = "Special")
option1L.grid(row=60,column=1, pady=10,sticky=tk.W, padx= 200)

option1E = tk.Entry(base,textvariable = specialNo, font=('arial',10))
option1E.grid(row=60,column=1, sticky=tk.W,pady=10, padx = 300)

def summation(sum):
    sum = lower + caps + special + numbers
    
# Building the password using these conditions
def randomize(sum):
    counter = 0
    while(sum > counter):
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


if(summation(sum) > 0 and summation(sum) < 20):
    randomize(sum)



base.mainloop()

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
