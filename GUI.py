import tkinter as tk
from tkinter import * 
import hashlib
import os
import time

limit = 100000

def take_input():
    message = input.get("1.0","end-1c")
    input.config(state="disabled")
    print(message)
    return message

    
def submit():
    try:
        message = take_input()
        diff = int(input_diff.get())
    except:
        update_output("Bitte geben Sie eine Nachricht UND eine Difficulty ein!")
    #print(message)
    else:
        findNonce(message, diff)

def update_output(text):
    output.insert(END, text)
    output.see("end")

def delete():
    input.config(state="normal") 
    input.delete("1.0", END)
    output.delete("1.0", END)
     
def findNonce(message, diff):
    global limit
    init_message = message
    output.insert(END, "searching Nonce for %s ... \n" %message)
    time.sleep(1)
    root.update()
    
    diff = str(str(0)*int(diff))
    
    print(diff)
    
    for nonce in range(0,limit):
        
        if nonce > 0:
            temp_message = str(init_message + str(nonce)).rstrip()
        else: 
            temp_message = str(init_message).rstrip()
            
        hash = hashlib.sha256(temp_message.encode()).hexdigest()
        text = hash + "\n"
        update_output(text)
        
        if hash.startswith(str(diff)):
            print("FOUND" , nonce, hash)
            text = "\n\n GEFUNDEN!! \n \n"
            update_output(text)
            text = str("\n\n" + temp_message + " ---> " + hash)
            update_output(text)
            
            break
        
    
    
if __name__ == "__main__":
    
    root = Tk()
    root.geometry("800x800")
    root.title("Proof-of-Work Jugend Forscht")
    root.config(bg="#f7931a")
    
    label_message = Label(text="Was ist deine Nachricht?")
    label_message.pack(pady=5)
    
    input = Text(root, height = 15, width = 75, bg = "light yellow")
    input.pack(pady=5)
    
    label_diff = Label(text="Geben sie eine Difficulty ein: ")
    label_diff.pack(pady=5)
        
    input_diff = Entry(root)
    input_diff.pack(pady=5)
    
    submit_button = Button(root, text="submit", command=submit)
    submit_button.pack(pady=5)
    
    clear_button = Button(root, text="clear", command=delete)
    clear_button.pack(pady=5)
    
    termf = Frame(root, height=400, width=500)

    
    output = Text(root, height = 50, width = 75, bg = "light yellow")
    output.pack(pady=5)
    
    
    
    root.mainloop()

