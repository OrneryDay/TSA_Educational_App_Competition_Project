import tkinter
from tkinter import Grid, Text, ttk, scrolledtext
from typing import Literal
from contextlib import suppress
from tkinter.messagebox import showinfo
from saveSys import *

"""
Made by Trent Struve
For the 2026-27 TSA software development competition
Wish me luck!
V0.5
inspired by Anki
"""


#constants for the window size specifications
VERSION="0.4"
VERSION_STAGE="pre-alpha"
WIDTH=750
LENGTH=520
MINWIDTH=750
MINLENGTH=520
MAXWIDTH=int(WIDTH*1.5)
MAXLENGTH=int(LENGTH*1.5)



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
    root.rowconfigure(16-1, pad=5, uniform=mainGroup, weight=2, minsize=20)
    
    return root

root = initRoot()

class testEntry:
    """Handles the test entry stuff. Saves the contents AFTER deletion, I might want to change that later.
    Access these contents directly from the instance's 'contents' attribute."""

    frame = tkinter.Frame(root)
    name = {}
    body = {}
    answer = {}
    sections = {}

    def __init__(self, original):
        self.frame = tkinter.Frame(root)
        self.name = {
            "label": tkinter.Label(self.frame, text="Enter your card name:"),
            "entry": Text(self.frame, height=1, wrap='word', width=25),
            "contents": str,
        }
        self.body = {
            "label": tkinter.Label(self.frame, height=2, text="Enter your card body:"),
            "entry": Text(self.frame, height=4, wrap='word', width=25, undo=True),
            "contents": str,
        }
        self.answer = {
            "label": tkinter.Label(self.frame, height=2, text="Enter your card answer:"),
            "entry": Text(self.frame, height=3, wrap='word', width=25, undo=True),
            "contents": str,
        }
        self.sections = {
            "name": self.name,
            "body": self.body,
            "answer": self.answer,
        }
        
        self.frame.grid(column=1, columnspan=2, row=0, rowspan=3)
        
        self.sections["name"]["label"].grid(column = 0, row = 0)
        self.sections["name"]["entry"].grid(column = 0, row = 1)
        
        self.sections["body"]["label"].grid(column = 0, row = 2)
        self.sections["body"]["entry"].grid(column = 0, row = 3)
        
        self.sections["answer"]["label"].grid(column = 0, row = 4)
        self.sections["answer"]["entry"].grid(column = 0, row = 5)
        
        

        
        tkinter.Button.configure(original, text="ACCEPT", command=lambda: self.testEntryEnd(original))

    def testEntryEnd(self, original):
        grabContents = lambda self: Text.get(self, "1.0", "end-1c")
        nameContents = (grabContents(self.sections["name"]["entry"])) # pyright: ignore[reportOptionalMemberAccess]
        bodyContents = (grabContents(self.sections["body"]["entry"])) # pyright: ignore[reportOptionalMemberAccess]
        answerContents = (grabContents(self.sections["answer"]["entry"])) # pyright: ignore[reportOptionalMemberAccess]

        if nameContents != "" and bodyContents != "" and answerContents != "":
            #tried a for loop to destroy, just returned strings that I can't do anything with.
            #sue me. I can just obliterate the frame, anyway, now that I think about it.
            self.frame.destroy()
            
            tkinter.Button.configure(original, state='disabled', text="ACCEPTED")
            saveCard(nameContents, bodyContents, answerContents)
            #showinfo("NEW CARD", )
            tkinter.Button.configure(original, state='normal', text="Create New Card", command=lambda: testEntry(original))




#   experimental segment, I want to see the boundaries of each cell.
#   doesn't work.
def debugGrid():
    for row in range(12):
        for col in range(7):
            frame = ttk.Frame(root, border=2, relief='ridge')
            frame.grid(column=col, row=row)
    
    
 
sideFrame = ttk.Frame(root, border=3, relief='ridge')
sideFrame.grid(column=0, row=0, sticky='w', rowspan=3)

testEntries = []
BUTTON_MAP ={
            0: ["Create New Card", lambda: testEntries.append(testEntry(testEntryButton))],
            1: ["Debug Print Children", lambda: list(map(print, tkinter.Tk.winfo_children(root)))],
            2: ["Debug Grid", lambda: debugGrid],
            3: ["Delete all Cards", lambda: clearCards()],
            4: ["QUIT", lambda: root.quit()]
            }


 #creates the side menu and returns the keepNums's corresponding buttons
mainMenuButtons = menu(BUTTON_MAP, sideFrame, [0])
testEntryButton = mainMenuButtons[0]

            
root.mainloop()
