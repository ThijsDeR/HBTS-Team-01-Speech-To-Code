from voiceFunctions import voiceFunctions
from codewriter import writeLine

class printFunctionality(voiceFunctions):
    toBePrintedText = ""
    printedText = ""
    def __init__(self, spacing):
        super().__init__(2, spacing)

    def advance(self, words, file):
        if "exit" in words:
            return True
        if "explain" in words:
            print(self.getFunctionalityString())
            self.SpeakText(self.getFunctionalityString())
            return False
        if "current sentence" in words:
            print(self.printedText)
            self.SpeakText(self.printedText)
            return False
        if "done" in words:
            self.printedText += self.toBePrintedText
            line = writeLine(file, f"print('{self.printedText}') \n", self.spacing)
            print(f"wrote `{line}` to the code")
            self.SpeakText(f"wrote `{line}` to the code")
            return True
        if self.currentStep == 0:
            print(self.getFunctionalityString())
            self.SpeakText(self.getFunctionalityString())
            self.currentStep = 1
        elif self.currentStep == 1:
            words = words.replace("add space ", " ")
            words = words.replace("new line", "\\n")
            self.toBePrintedText = words.replace("print ", "")
            print(f"are you happy with the text: \n {self.printedText + self.toBePrintedText} (say add, remove or done)")
            self.SpeakText(f"are you happy with the text: \n {self.printedText + self.toBePrintedText} (say add, remove, or done)")
            self.currentStep = 2
        elif (self.currentStep == 2):
            if "add" in words:
                self.currentStep = 1
                print("Back to step 1")
                self.printedText += self.toBePrintedText
                self.SpeakText("Back to step 1")
                return False
            elif "remove" in words:
                self.currentStep = 1
                print("Back to step 1, removing")
                self.SpeakText("Back to step 1, removing")
                return False
            elif "done" in words:
                self.printedText += self.toBePrintedText
                line = writeLine("text.py", f"print('{self.printedText}') \n", self.spacing)
                print(f"wrote `{line}` to the code")
                self.SpeakText(f"wrote `{line}` to the code")
                return True
            else:
                print("Nothing found, try again")
                self.SpeakText("Nothing found, try again")
            self.toBePrintedText = ""
    def getFunctionalityString(self):
        return "Step one is say 'print [words you want to print]'"