from voiceFunction import voiceFunctions

class



def whileFunction(words, file):
    if (self.Currentstep == 1)
    f = open(file, "a")
    if "while" in words:
        print("Pleade give the first variable:")
        var1 = words.replace("while", "")

        # hier moet een call functie komen

        print('please give the operator')
        if "greater than" in words:
            operator = words.replace(">", "")
        elif "greater than or equal to" in words:
            operator = words.replace(">=", "")
        elif "less than" in words:
            operator = words.replace("<", "")
        elif "less than or equal to" in words:
            operator = words.replace("<=", "")
        elif "equal" in words:
            operator = words.replace("==", "")
        elif "not equal" in words:
            operator = words.replace("!=", "")

            # hier moet een call functie komen

        print("Please give the second variable:")
        var2 = words.replace("", "")
        f.write(f"\n while('{var1} {operator} {var2} ') \n")
    f.close()