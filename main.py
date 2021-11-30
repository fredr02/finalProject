from tkinter import *

root = Tk()
root.title("Fred's Final Project")  
root.geometry("500x500")

def mainMenu():
  mainFrame = LabelFrame(root, text="Main Menu", padx=30, pady = 30)
  mainFrame.pack(pady= 150)

  btn_verifyISBN10 = Button(mainFrame, text = "1. Verify the check digit of an ISBN-10", command = lambda: [mainFrame.forget(), verifyISBN10()])
  btn_verifyISBN13 = Button(mainFrame, text = "2. Verify the check digit of an ISBN-13", command = lambda: [mainFrame.forget(), verifyISBN13()])
  btn_convertI10toI13 = Button(mainFrame, text = "3. Convert an ISBN-10 to an ISBN-13", command = lambda: [mainFrame.forget(), convertI10toI13()])
  btn_convertI13toI10 = Button(mainFrame, text = "4. Convert an ISBN-13 to an ISBN-10", command = lambda: [mainFrame.forget(), convertI13toI10()])
 
  btn_verifyISBN10.pack()
  btn_verifyISBN13.pack()
  btn_convertI10toI13.pack()
  btn_convertI13toI10.pack()
  # index = 0
  # for x in mainButtons:
  #   button = Button(mainFrame, text = x, command = lambda: [mainFrame.forget(),print(commands[index]), commands[index]])
  #   index = index + 1
  #   button.pack()
  root.mainloop() 

def verifyISBN10():
  verifyISBN10_Frame = LabelFrame(root, text="Verify ISBN 10", padx=30, pady = 30)
  verifyISBN10_Frame.pack()

def verifyISBN13():
  verifyISBN13_Frame = LabelFrame(root, text="Verify ISBN 13", padx=30, pady = 30)
  verifyISBN13_Frame.pack()
  
def convertI10toI13():
  convertI10toI13_Frame = LabelFrame(root, text="Convert I10 to I13", padx=30, pady = 30)
  convertI10toI13_Frame.pack()

def convertI13toI10():
  convertI10toI10_Frame = LabelFrame(root, text="Convert I13 to I10", padx=30, pady = 30)
  convertI10toI10_Frame.pack()
  
mainMenu()