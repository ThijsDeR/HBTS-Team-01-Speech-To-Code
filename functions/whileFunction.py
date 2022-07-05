from voiceFunctions import voiceFunctions

class whileFunctionality(voiceFunctions):
    toBePrintedText = ""
    def __init__(self):
        super().__init__(3)

    def advance(self, words, file):
        if "exit while" in words:
            return True

        if "explain while" in words:
            print(self.getFunctionalityString())
            self.SpeakText(self.getFunctionalityString())
            return False

        if self.currentStep == 1:       
            f = open(file, "a")
        if "while" in words:
            self.toBePrintedText = words.replace("while", "")
            f.close()

            self.currentStep = 2
        if (self.currentstep == 2):
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
            
            f.write(f"\n while('{var1} {operator} {var2} ') \n")

            # hier moet een call functie komen
            self.currentStep = 3
        if (slef.currentstep == 3):    
            print("Please give the second variable:")
            var2 = words.replace("", "")
            f.write(f"\n while('{var1} {operator} {var2} ') \n")
        f.close()

    def getFunctionalityString(self):
        return "Step one is say 'while, then you will get a option for a variable and after that you can choose the operator and second variable"