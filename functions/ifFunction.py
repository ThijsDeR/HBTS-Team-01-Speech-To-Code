from voiceFunctions import voiceFunctions

class ifFunctionality(voiceFunctions):
    toBePrintedText = ""
    def __init__(self):
        super().__init__(5)

    def advance(self, words, file):
        if "exit" in words:
            return True

        if "explain" in words:
            print(self.getFunctionalityString())
            self.SpeakText(self.getFunctionalityString())
            return False
            
        if self.currentStep == 1:
            f = open(file, "a")
            if "if" in words:
                self.toBePrintedText = words.replace("if ", "")
            f.close()
            self.currentStep = 2

        if self.currentStep == 2:
            print("Please give the first variable:")
            variable1 = words.replace("")
            f.close()
            print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.currentStep = 3

        if self.currentStep == 3:
            print("Please give the operator:")
            if "equals" in words:
                operator = words.replace("==")
            elif "not equals" in words:
                operator = words.replace("!=")
            elif "less than" in words:
                operator = words.replace("<")
            elif "less than or equals to" in words:
                operator = words.replace("<=")
            elif "greater than" in words:
                operator = words.replace(">")
            elif "greater than or equals to" in words:
                operator = words.replace(">=")
            f.close()
            print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.currentStep == 4

        if self.currentStep == 4:
            print("Please give the second variable:")
            variable2 = words.replace("")
            f.close()
            print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.currentStep == 5
            
        if (self.currentStep == 5):
            if "yes" in words:
                f = open(file, "a")
                f.write(f"print('{self.toBePrintedText}') \n")
                f.close()
                print(f"wrote `print('{self.toBePrintedText}')` to the code")
                self.SpeakText(f"wrote `if('{variable1} + {operator} + {variable2}')` to the code")
                return True
            elif "no" in words:
                self.currentStep = 1
                print("Back to step 1")
                self.SpeakText("Back to step 1")
                return False

    def getFunctionalityString(self):
        return "Step one is say 'if'.\n Step 2 is say [variable 1].\n Step 3 is say [operator].\n Step 4 is say [variable 2]."
            