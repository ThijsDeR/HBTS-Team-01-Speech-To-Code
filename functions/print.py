from voiceFunctions import voiceFunctions


class printFunctionality(voiceFunctions):
    toBePrintedText = ""
    addSetting = False
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
                words = words.replace("new line", "\\n")
                if self.addSetting:
                    self.toBePrintedText += words.replace("print ", "")
                    print(self.toBePrintedText)
                else:
                    self.toBePrintedText = words.replace("print ", "")
                    print(self.toBePrintedText)
            f.close()
            print(f"are you happy with the text: \n {self.toBePrintedText} (say add, restart or done)")
            self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say add, restart, or done)")

            self.currentStep = 2
        elif (self.currentStep == 2):
            if "add" in words:
                self.currentStep = 1
                print("Back to step 1, addition on")
                self.SpeakText("Back to step 1, addition on")
                self.addSetting = True
                return False
            elif "restart" in words:
                self.currentStep = 1
                print("Back to step 1, restarting")
                self.SpeakText("Back to step 1, restarting")
                self.addSetting = False
                return False
            elif "done" in words:
                f = open(file, "a")
                f.write(f"print('{self.toBePrintedText}') \n")
                f.close()
                print(f"wrote `print('{self.toBePrintedText}')` to the code")
                self.SpeakText(f"wrote `print('{self.toBePrintedText}')` to the code")
                return True
            else:
                print("Nothing found, try again")
                self.SpeakText("Nothing found, try again")
    def getFunctionalityString(self):
        return "Step one is say 'print [words you want to print]'"
            