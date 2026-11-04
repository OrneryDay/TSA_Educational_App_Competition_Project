import tkinter
from tkinter import Grid, Text, ttk, scrolledtext
from typing import Literal

"""
Made by Trent Struve
For the 2026-27 TSA software development competition
Wish me luck!
V0.3
inspired by Anki
"""


#constants for the window size specifications
VERSION="0.3"
VERSION_STAGE="pre-alpha"
WIDTH=750
LENGTH=500
MINWIDTH=750
MINLENGTH=500
MAXWIDTH=WIDTH
MAXLENGTH=LENGTH



def menu(buttonMap: dict, parent, keepNums: list[int]):
    """
        puts to the grid all of the buttons in the buttonMap dictionary.
        
        buttonMap entries MUST be ordered by number, starting from 0.
        Position of entries within the dictionary is irrelevant, eg. [1, 5, 4, 2, 3, 0] works just fine.
        
        Args:
            buttonMap: a dictionary of buttons to be displayed.
            parent: the parent widget where the buttons will be placed.
            keepNums: the IDs of the buttons that should be returned in the returnArray.

        Returns:
            returnArray: a list of the buttons kept according to keepNums.
    """
    
    #these arrays must all be the same length.
    returnArray = []
    for x in range(len(buttonMap)):#for [every option]
        #creates a column of buttons along the left hand side
        button = ttk.Button  (parent,
                    text=buttonMap[x][0], #0 for the name
                    padding=25,
                    command=lambda x=x: buttonMap[x][1]() #1 for the command and arguments
                    )
        if x in keepNums:
            returnArray.append(button)
        button.grid(column=0, row=x, sticky='ew')
        for widget in parent.winfo_children():
            widget.grid(padx=2, pady=5) # pyright: ignore[reportCallIssue]
        #return parent.winfo_children()
    return returnArray
        

    

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

class testEntry:
    """Handles the test entry stuff. Saves the contents AFTER deletion, I might want to change that later.
    Access these contents directly from the instance's 'contents' attribute."""
    entry = None
    label = None
    contents = None
    def __init__(self, original):
        self.entry = Text(root, height=10, wrap='word', width=25)
        self.entry.grid(column = 1, row = 1, columnspan=1)
        self.label = tkinter.Label(root, text="Enter your card content:")
        self.label.grid(column = 1, row = 0)
            
        
        tkinter.Button.configure(original, text="ACCEPT", command=lambda: self.testEntryEnd(original))

    def testEntryEnd(self, original):
        contents = (self.entry.get("1.0", "end-1c")) # pyright: ignore[reportOptionalMemberAccess]
        print(type(self.entry)) # pyright: ignore[reportOptionalMemberAccess]
        if contents != "":
            self.entry.destroy() # pyright: ignore[reportOptionalMemberAccess]
            self.label.destroy() # pyright: ignore[reportOptionalMemberAccess]
            self.contents = contents
            print(contents)
            tkinter.Button.configure(original, state='disabled', text="ACCEPTED")

#   experimental segment, I want to see the boundaries of each cell.
#   doesn't work.
def debugGrid():
    for row in range(12):
        for col in range(7):
            frame = ttk.Frame(root, border=2, relief='ridge')
            frame.grid(column=col, row=row)
    
    
 
root = initRoot()
sideFrame = ttk.Frame(root, border=3, relief='ridge')
sideFrame.grid(column=0, row=0, sticky='w', rowspan=3)

frameChildren = []
BUTTON_MAP ={
            0: ["Create New Card", lambda: testEntry(testEntryButton)],
            1: ["Debug Print Children", lambda: list(map(print, tkinter.Tk.winfo_children(root)))],
            2: ["Debug Grid", lambda: debugGrid],
            3: ["Button 4", lambda: print("option 4")],
            4: ["QUIT", lambda: root.quit()]
            }


 #creates the side menu and returns the keepNums's corresponding buttons
testEntryButton = menu(BUTTON_MAP, sideFrame, [0])[0]

            
root.mainloop()
