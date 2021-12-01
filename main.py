from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.title("Fred's Final Project")
root.geometry("400x600")


def mainMenu():
    mainFrame = LabelFrame(root, text="Main Menu", padx=30, pady=30)
    mainFrame.pack(pady=150)

    menuNames = ["Verify the check digit of an ISBN-10", "Verify the check digit of an ISBN-13",
                 "Convert an ISBN-10 to an ISBN-13", "Convert an ISBN-13 to an ISBN-10"]

    for index, menu in enumerate(menuNames):
        btn = Button(mainFrame, text=menuNames[index],
                     command=lambda: [mainFrame.forget(), item_Menu(menu)]).grid(row=index, column=0)


def item_Menu(itemName):
    itemFrame = LabelFrame(
        root, text=itemName, padx=30, pady=30)
    itemFrame.pack()

    openFileButton = Button(itemFrame, text="Open ISBN List",
                            command=lambda: askopenfilename()).grid(row=0, column=0)

    back = Button(itemFrame, text="Back", command=lambda: [
        itemFrame.forget(), mainMenu()]).grid(row=1, column=0)


def createFile():
    print(open(askopenfilename()).read())


mainMenu()
root.mainloop()
