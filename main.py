from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.title("ISBN Tool")

Label(root, pady=10, text="ISBN Tool", font=(
    "Arial", 20),).pack()
root.geometry("400x600")


def mainMenu():
    mainFrame = LabelFrame(root, text="Main Menu", padx=30, pady=30)
    mainFrame.pack(pady=150)

    menuNames = ["Verify the check digit of an ISBN-10", "Verify the check digit of an ISBN-13",
                 "Convert an ISBN-10 to an ISBN-13", "Convert an ISBN-13 to an ISBN-10"]

    for index, menu in enumerate(menuNames):
        btn = Button(mainFrame, text=menuNames[index],
                     command=lambda menu=menu: [mainFrame.forget(), item_Menu(menu)]).grid(row=index, column=0)


def item_Menu(itemName):
    itemFrame = LabelFrame(
        root, text=itemName, padx=30, pady=30)
    itemFrame.pack(pady=150)

    # Label to indicate Status
    Label(itemFrame, text="Awaiting List", font=(
        "Arial", 20),).grid(row=0, column=0)

    # Button To Open File
    Button(itemFrame, text="Open ISBN List",
           command=lambda: createFile(itemName)).grid(row=1, column=0, sticky=N)

    # Button to go back
    Button(itemFrame, text="↩", width=1, command=lambda: [
        itemFrame.forget(), mainMenu()]).grid(row=4, column=0)


def createFile(itemName):
    print(open(askopenfilename()).read())


mainMenu()
root.mainloop()
