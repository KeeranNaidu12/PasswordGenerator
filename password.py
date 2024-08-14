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

# Building the password using these conditions
def randomize():
    lower = lowerNo.get()
    caps = capsNo.get()
    special = specialNo.get()
    numbers = numbersNo.get()
    counter = lower + caps + special + numbers

    if counter > 20:
        generated.config(text=" The total characetrs selcted exceeds the password limit! Try again")
        return

    char = []

    char.extend(random.choice("abcdefghijklmnopqrstuvwxyz",k=lower))
    char.extend(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=caps))
    char.extend(random.choice("0123456789",k=numbers))
    char.extend(random.choice("+-=*&^%$#@!?><",k=special))

    random.shuffle(char)
    password = ''.join(char)

    button.config(text="Your password is: " + password)



# Window title and Dimensions
base.title("Python Password Generator")
base.geometry("650x1600")


# Labels with what the program is about and basic instructions
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

option2L = tk.Label(base,text = "Captials")
option2L.grid(row=40,column=1, pady=10,sticky=tk.W, padx= 200)

option2E = tk.Entry(base,textvariable = capsNo, font=('arial',10))
option2E.grid(row=40,column=1, sticky=tk.W,pady=10, padx = 300)

option3L = tk.Label(base,text = "Numbers")
option3L.grid(row=50,column=1, pady=10,sticky=tk.W, padx= 200)

option3E = tk.Entry(base,textvariable = numbersNo, font=('arial',10))
option3E.grid(row=50,column=1, sticky=tk.W,padx = 300, pady=10)

option4L = tk.Label(base,text = "Special")
option4L.grid(row=60,column=1, pady=10,sticky=tk.W, padx= 200)

option4E = tk.Entry(base,textvariable = specialNo, font=('arial',10))
option4E.grid(row=60,column=1, sticky=tk.W,pady=10, padx = 300)

# Button to generate the password
button = tk.Button(base, text = "Generate a Password",command=randomize)
button.grid(row=90,column=1, sticky=tk.W,pady=10, padx = 300)

# Display message indicating the password generation
generated = tk.Label(base, text="")
generated.grid(row=110,column=1, sticky=tk.W,pady=10, padx = 300)

base.mainloop()
