from voiceFunctions import voiceFunctions


class printFunctionality(voiceFunctions):
    toBePrintedText = ""
    def __init__(self):
        super().__init__(2)

    def advance(self, words, file):
        if "exit" in words:
            return True
        if "explain" in words:
            print(self.getFunctionalityString())
            self.SpeakText(self.getFunctionalityString())
            return False
        if self.currentStep == 1:
            f = open(file, "a")
            if "print" in words:
                self.toBePrintedText = words.replace("print ", "")
            f.close()
            print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")

            self.currentStep = 2
        if (self.currentStep == 2):
            if "yes" in words:
                f = open(file, "a")
                f.write(f"print('{self.toBePrintedText}') \n")
                f.close()
                print(f"wrote `print('{self.toBePrintedText}')` to the code")
                self.SpeakText(f"wrote `print('{self.toBePrintedText}')` to the code")
                return True
            elif "no" in words:
                self.currentStep = 1
                print("Back to step 1")
                self.SpeakText("Back to step 1")
                return False
    def getFunctionalityString(self):
        return "Step one is say 'print [words you want to print]'"
            