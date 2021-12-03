from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

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
    labelText = StringVar()
    labelText.set("Awaiting List")
    Label(itemFrame, textvariable=labelText, font=(
        "Arial", 20),).grid(row=0, column=0)

    # Button To Open File
    Button(itemFrame, text="Open ISBN List",
           command=lambda: openFile(itemName, labelText, itemFrame)).grid(row=1, column=0, sticky=N)

    # Button to go back
    Button(itemFrame, text="↩", width=1, command=lambda: [
        itemFrame.forget(), mainMenu()]).grid(row=4, column=0)


def openFile(itemName, labelText, itemFrame):
    file = open(askopenfilename())
    saveFile = ""
    for line in file:
        if itemName == "Verify the check digit of an ISBN-10":
            saveFile += verifyISBN10(line)
        elif itemName == "Verify the check digit of an ISBN-13":
            saveFile += verifyISBN13(line)
        elif itemName == "Convert an ISBN-10 to an ISBN-13":
            saveFile += convert10to13(line)
        elif itemName == "Convert an ISBN-13 to an ISBN-10":
            saveFile += convert13to10(line)
    print(saveFile)

    labelText.set("Ready to save!")
    Button(itemFrame, text="Save File", command=lambda: [open(asksaveasfilename(), "w").write(saveFile), labelText.set("File Was Saved")]).grid(
        row=2, column=0, sticky=N)


def verifyISBN10(isbn):
    # Clean ISBN numbers
    isbn.replace("-", "").replace(" ", "")

    result = 0
    for i in range(9):
        result = result + int(isbn[i]) * (10 - i)

    checkDigit = 11 - (result % 11)

    isbn[9].lower()
    # Return modified line depending on correctness
    if checkDigit == 10 and isbn[9].lower() == "x":
        return (isbn).rstrip("\n") + " Correct Check ISBN10 Digit\n"
    if (checkDigit) == int(isbn[9]):
        return (isbn).rstrip("\n") + " Correct Check ISBN10 Digit\n"
    else:
        return (isbn).rstrip("\n") + " Incorrect Check ISBN10 Digit\n"


def verifyISBN13(isbn):
    # Clean ISBN numbers
    isbn.replace("-", "").replace(" ", "")

    result = 0
    for i in range(12):
        if i % 2 == 0:
            result = result + int(isbn[i])
        else:
            result = result + int(isbn[i]) * 3

    if 10 - (result % 10) == int(isbn[12]):
        return (isbn).rstrip("\n") + " Correct ISBN13 Digit\n"
    else:
        return (isbn).rstrip("\n") + " Incorrect ISBN13 Check Digit\n"


def convert10to13(isbn):
    isbn.replace("-", "").replace(" ", "")
    preCheckDigitISBN13 = "978" + isbn[:-1]

    result = 0
    for i in range(12):
        if i % 2 == 0:
            result = result + int(preCheckDigitISBN13[i])
        else:
            result = result + int(preCheckDigitISBN13[i]) * 3
    final = preCheckDigitISBN13 + str(10 - (result % 10))
    return final + " Calculated ISBN13 Number\n"


def convert13to10(isbn):
    isbn.replace("-", "").replace(" ", "")
    isbn = isbn[3:12]

    result = 0
    for i in range(9):
        result = result + int(isbn[i]) * (10 - i)

    checkDigit = 11 - (result % 11)
    if checkDigit == 10:
        checkDigit = "x"

    return isbn + checkDigit + " Calculated ISBN10 Number\n"


mainMenu()
root.mainloop()
