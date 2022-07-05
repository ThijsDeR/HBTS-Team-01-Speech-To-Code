from traceback import print_tb


def printFunction(words, file):
    f = open(file, "a")
    if "while" in words:
        print("Pleade give the first variable:")
        var1 = words.replace("while", "")

        print('please give operator')
        if "bigger" in words:
            operator = words.replace(">", "")
        elif "bigger or equal" in words:
            operator = words.replace(">=", "")
        elif "smaller" in words:
            operator = words.replace("<", "")
        elif "smaller or equal" in words:
            operator = words.replace("<=", "")
        elif "equal" in words:
            operator = words.replace("==", "")
        elif "not equal" in words:
            operator = words.replace("!=", "")


        print("Please give the second variable:")
        var2 = words.replace("")

        f.write(f"\n  while('{var1} {operator} {var2} ') \n")
    f.close()