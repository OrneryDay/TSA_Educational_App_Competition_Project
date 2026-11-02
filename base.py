import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMenu
#^^^ remember that these libraries all start with Q ^^^ (and maybe clean it up a bit)
from PySide6.QtCore import QSize, Qt

"""
whatever you put here
"""

APP_NAME = "app"
WIDGET_MAX_X = 325
WIDGET_MAX_Y = 300


class MainWindow(QMainWindow):
    button2 = None
    def __init__(self): #I think the self argument is solely for that final line...
        super().__init__()

        self.setWindowTitle(APP_NAME)
        
        self.setMinimumSize(QSize(WIDGET_MAX_X*.25, WIDGET_MAX_Y*.25)) #minimum is 25% of the maximum
        self.setMaximumSize(QSize(WIDGET_MAX_X, WIDGET_MAX_Y))

        # Set the central widget of the Window.
        button = QPushButton("click me already."); self.setCentralWidget(button)
        self.buttonToggled = False
        
        button.setCheckable = True
        button.clicked.connect(self.onButtonClicked)
        #menu = self.QMenu()
        
    
    def createMainMenu(window):
        button1 = QPushButton("Press Me!")
        
        
        menu = window.menuBar()
        
        menu = menu.addMenu("File")
        menu.addAction(1, button1)
        

        
        
        
    class mainButton:
        '''
        handles this main button. Made up of instance-only calls.
            __init__:
                self: instance
                returns: the instance
            onButtonClicked:
                checks the button as clicked
            buttonChecked:
                checks the checked/unchecked state of the button
                or something, idk
        
        '''
        button2 = None
        
        def __init__(self):
            button2 = QPushButton("no, press ME!")
            button2.setCheckable(True)
            button2.clicked.connect(self.onButtonClicked)
        
        def onButtonClicked(self):
            print("button was clicked.")
            self.buttonChecked()
            
        def checked(self): 
            return self.button_is_checked()
            
        
        


app = QApplication(sys.argv)


window = MainWindow() #remember that this passes self (window) as an argument
#window.createMainMenu() #stay away from this one for now
window.show()

app.exec()
