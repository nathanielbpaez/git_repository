def repeat():
    x = str(input("Would you like to calculate more (Y/N)?: "))
    if x == "Y":
        print("Lol")
    elif x == "N":
        print("Nah")
    else:
        print('Incorrect input please try again.')
        return repeat()
    return

repeat()