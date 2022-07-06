from voiceFunctions import voiceFunctions

class forFunctionality(voiceFunctions):
    toBePrintedText = ""
    def __init__(self):
        super().__init__(3)

    def advance(self, words, file):
        if "exit for" in words:
            return True

        if "explain for" in words:
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
        if any in words:
              function = words.replace(any)
        elif "range one" in words:
             function = words.replace("range(1)")
        elif "range two" in words:
             function = words.replace("range(2)")
        elif "range three" in words:
             function = words.replace("range(3)")
        elif "range four" in words:
             function = words.replace("range(4)")
        elif "range five" in words:
             function = words.replace("range(5)")
        elif "range six" in words:
             function = words.replace("range(6)")
             f.close()
             print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
             self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
             self.currentStep = 3
            
        print("printing")
                # hier moet een call functie komen
     
        if (self.currentstep == 3): 
          print("printing")   
        f.write(f"\n  'for x in {function}: print('x')'; \n")
        f.close()
        print(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
        self.SpeakText(f"are you happy with the text: \n {self.toBePrintedText} (say yes or no)")
        
    def getFunctionalityString(self):
        return "Step one is say 'while, then you will get a option for a variable and after that you can choose the operator and second variable"
