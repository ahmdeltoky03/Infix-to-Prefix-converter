from infix_to_prefix import *
import customtkinter as ctk
import tkinter #this is incase a widget isnt added to custom tkinter
from prefix_evaluation import *


# This is the main body of the app and it renders the gui and listens for clicks and do on
# it is made using customtkinter 
def main():
    
    
    # this nested function takes values from the textbox and manipulates
    # the value of the output label using the functions that solve the expression
    def calc ():
        prefix = infix_to_prefix(entry.get("0.0",tkinter.END))
        result = prefixEvaluation(prefix)
        label1.configure(text=f"{prefix}\n\n{result}")
    
    
    window = ctk.CTk()       # init a window using ctk 
    window.title("Infex to Prefix")     

    ctk.set_default_color_theme("dark-blue") #set its theme(though it doesnt matter since darkblue is default)

    frame=ctk.CTkFrame(window) # create a frame to house the grid of widgets
    frame.pack(side="left", expand=True,padx=20,pady=20) # add padding(the rest isnt apparent in our usecase)

    label = ctk.CTkLabel(frame,text="Enter Equation")#create a label
    # I use a grid to organize the various elements 
    label.grid(row=0,column=0,padx=10,pady=10)

    entry = ctk.CTkTextbox(frame,height=10)# create a textbox next to the label
    entry.grid(row=0,column=1,padx=10,pady=10)

    # add a button that calls the nested function calc
    button = ctk.CTkButton(frame,text="Calculate",command=lambda:calc(),)
    button.grid(row=1,column=0,columnspan=2,rowspan=2,padx=10,pady=10)

    # add a big label that serves as the output screen
    label1=ctk.CTkLabel(frame,text="",width=100,height=100,bg_color="#333333",padx=20,pady=20)
    label1.grid(row=0,column=2,rowspan=3,padx=20,pady=20,sticky="nsew")
    #sticky NSEW makes it expand in all directions
    
    # this starts the rendering and listening of the window 
    # and stops the excution of anything after it
    window.mainloop()

    
    
# this is here just for structure    
main()

# next file => ./infex_to_prefix.py