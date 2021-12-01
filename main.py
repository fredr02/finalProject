from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.title("Fred's Final Project")  
root.geometry("400x600")

def mainMenu():
  mainFrame = LabelFrame(root, text="Main Menu", padx=30, pady = 30)
  mainFrame.pack(pady= 150)

  btn_verifyISBN10 = Button(mainFrame, text = "1. Verify the check digit of an ISBN-10", command = lambda: [mainFrame.forget(), verifyISBN10_Menu()]).grid(row=0, column=0)
  btn_verifyISBN13 = Button(mainFrame, text = "2. Verify the check digit of an ISBN-13", command = lambda: [mainFrame.forget(), verifyISBN13_Menu()]).grid(row=1, column=0)
  btn_convertI10toI13 = Button(mainFrame, text = "3. Convert an ISBN-10 to an ISBN-13", command = lambda: [mainFrame.forget(), convertI10toI13_Menu()]).grid(row=2, column=0)
  btn_convertI13toI10 = Button(mainFrame, text = "4. Convert an ISBN-13 to an ISBN-10", command = lambda: [mainFrame.forget(), convertI13toI10_Menu()]).grid(row=3, column=0)
 
  root.mainloop() 

def verifyISBN10_Menu():
  verifyISBN10_Frame = LabelFrame(root, text="Verify ISBN 10", padx=30, pady = 30)
  verifyISBN10_Frame.pack()

  openFile = Button(verifyISBN10_Frame, text = "Open ISBN List", command = lambda: askopenfilename()).grid(row=0,column=0)

  back = Button(verifyISBN10_Frame, text = "Back", command = lambda: [verifyISBN10_Frame.forget(), mainMenu()]).grid(row=1,column=0)

def verifyISBN13_Menu():
  verifyISBN13_Frame = LabelFrame(root, text="Verify ISBN 13", padx=30, pady = 30)
  verifyISBN13_Frame.pack()

  openFile = Button(verifyISBN13_Frame, text = "Open ISBN List", command = lambda: askopenfilename()).grid(row=0,column=0)

  back = Button(verifyISBN13_Frame, text = "Back", command = lambda: [verifyISBN13_Frame.forget(), mainMenu()]).grid(row=1,column=0)
  
def convertI10toI13_Menu():
  convertI10toI13_Frame = LabelFrame(root, text="Convert I10 to I13", padx=30, pady = 30)
  convertI10toI13_Frame.pack()

  openFile = Button(convertI10toI13_Frame, text = "Open ISBN List", command = lambda: askopenfilename()).grid(row=0,column=0)
  
  back = Button(convertI10toI13_Frame, text = "Back", command = lambda: [convertI10toI13_Frame.forget(), mainMenu()]).grid(row=1,column=0)

def convertI13toI10_Menu():
  convertI10toI10_Frame = LabelFrame(root, text="Convert I13 to I10", padx=30, pady = 30)
  convertI10toI10_Frame.pack()

  openFile = Button(convertI10toI10_Frame, text = "Open ISBN List", command = lambda: askopenfilename()).grid(row=0,column=0)

  back = Button(convertI10toI10_Frame, text = "Back", command = lambda: [convertI10toI10_Frame.forget(), mainMenu()]).grid(row=1,column=0)
  
mainMenu()