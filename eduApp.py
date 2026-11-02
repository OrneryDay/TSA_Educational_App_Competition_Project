import tkinter
from tkinter import Grid, Text, ttk
from typing import Literal

"""
Made by Trent Struve
For the 2026-27 TSA software development competition
Wish me luck!
V0.2
inspired by Anki
"""


#constants for the window size specifications
VERSION="0.2"
VERSION_STAGE="pre-alpha"
WIDTH=750
LENGTH=500
MINWIDTH=750
MINLENGTH=500
MAXWIDTH=1000
MAXLENGTH=800



def menu(buttonMap: dict, parent):
    """
        puts to the grid all of the buttons in the buttonMap dictionary.
        
        buttonMap entries MUST be ordered by number, starting from 0.
        Position of entries within the dictionary is irrelevant, eg. [1, 5, 4, 2, 3, 0] works just fine.
    """
    
    #these arrays must all be the same length.

    for x in range(len(buttonMap)):#for [every option]
        #creates a column of buttons along the left hand side
        button = ttk.Button  (parent,
                    text=buttonMap[x][0], #0 for the name
                    padding=25,
                    command=lambda x=x: buttonMap[x][1]() #1 for the command and arguments
                    )
        button.grid(column=0, row=x, sticky='ew')
        for widget in parent.winfo_children():
            widget.grid(padx=2, pady=5) # pyright: ignore[reportCallIssue]
        #return parent.winfo_children()
        

    

def initRoot():
    root = tkinter.Tk()
    root.title(f"Educational Software v{VERSION} ({VERSION_STAGE})")
    root.geometry(f"{WIDTH}x{LENGTH}+0+0")
    root.minsize(MINWIDTH, MINLENGTH)
    root.maxsize(MAXWIDTH, MAXLENGTH)
    
    mainGroup = "group1"
    # num-1 because typical index rules; 0 = 1
    root.columnconfigure(8-1,pad=15, uniform=mainGroup, weight=1, minsize=250)
    root.rowconfigure(12-1, pad=30, uniform=mainGroup, weight= 2, minsize=20)
    
    return root


def testEntryInit():
    global entry
    entry = tkinter.Text(root, height=2)
    acceptButton = ttk.Button(root, text="Accept", command=lambda: root.quit())
    entry.grid(column = 1, row = 0, columnspan=3)
    acceptButton.grid(column=1, row=1)
    
#experimental segment, I want to see the boundaries of the grid.
def debugGrid():
    for row in range(12):
        for col in range(7):
            frame = ttk.Frame(root, border=5, relief='ridge')
            frame.grid(column=col, row=row)
    
 
root = initRoot()
sideFrame = ttk.Frame(root, border=3, relief='ridge')
sideFrame.grid(column=0, row=0, sticky='w', rowspan=3)

frameChildren = []
BUTTON_MAP ={
            0: ["button 1", testEntryInit],
            1: ["debug print children", lambda: list(map(print, tkinter.Tk.winfo_children(root)))],
            2: ["debug grid", lambda: debugGrid],
            3: ["button 4", lambda: print("option 4")],
            4: ["QUIT", lambda: root.quit()]
            }

#print(root.grid_size()) #debug



menu(BUTTON_MAP, sideFrame)

            
root.mainloop()
