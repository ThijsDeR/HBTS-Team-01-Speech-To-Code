from voiceFunctions import voiceFunctions

class forFunctionality(voiceFunctions):
    toBePrintedText = ""
    def __init__(self):
        super().__init__(3)

    def advance(self, words, file):
        if "exit" in words:
            return True

        if "explain" in words:
            print(self.getFunctionalityString())
            self.SpeakText(self.getFunctionalityString())
            return False

        if self.currentStep == 1:       
            f = open(file, "a")
            if "for" in words:
                self.toBePrintedText = words.replace("for", "")
                f.close()

            self.currentStep = 2
        if (self.currentstep == 2):
            print('please give the operator')
            if "index" in words:
                forloopindex = words.replace("i")
            elif "equals" in words:
                equals = words.replace("=")
            elif "one" in words:
                forloopnumber = words.replace("1")
            elif "zero" in words:
                forloopnumber = words.replace("0")
            elif "greater than" in words:
                operator = words.replace(">")
            elif "less than" in words:
                operator = words.replace("<")
            elif "less than or equals to" in words:
                operator = words.replace("<=")
            elif "greater than or equals to" in words:
                operator = words.replace("=>")
            elif "plus" in words:
                addorless = words.replace("++")
            elif "minus" in words:
                addorless = words.replace("--")
            elif "bracket" in words:
                bracket = words.replace("{}")
                f.close()
                print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
                self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
                self.currentStep = 3
            # hier moet een call functie komen
     
        if (self.currentstep == 3): 
            f.write(f"\n  'for( let {forloopindex} {equals} {forloopnumber}; {forloopindex} {operator} array.length; {forloopindex}{addorless}) {bracket} '; \n")
            f.close()
            print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
            self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
        
    def getFunctionalityString(self):
        return "Step one is say 'while, then you will get a option for a variable and after that you can choose the operator and second variable"
#     for (let index = 0; index < array.length; index++) {
#     const element = array[index];
# }