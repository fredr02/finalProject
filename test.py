test = input()


def verifyISBN10(test):
    result = 0
    for i in range(9):
        result = result + int(test[i]) * (10 - i)

    if test[9].lower() == "x":
        result += 10
    else:
        result += int(test[9])
    print(result % 11)


verifyISBN10(test)
