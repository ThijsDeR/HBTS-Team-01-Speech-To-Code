# def dataFunction(words, file):
#     f = open(file, "a")
#     if "data type" in words:
#         if "string" in words:
#             printedText = words.replace("data type string ", "")
#             print("data type = string")
#             f.write(f"\n  string = '{printedText}' \n")
#         elif "array" in words:
#             printedText = words.replace("data type array ", "")
#             print("data type = array")
#             f.write(f"\n  array = [{printedText}] \n")
#     f.close()

from voiceFunctions import voiceFunctions

class dataFunctionality(voiceFunctions):
    newVar = ""
    varData = ""
    addSetting = False
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
            if "name" in words:
                words = words.replace("new line", "\\n")
                self.newVar += words.replace("name ", "")
                print(self.newVar)
            else:
                print("Nothing found, try again")
                self.SpeakText("Nothing found, try again")

            f.close()
            self.currentStep == 2


        if self.currentStep == 2:
            print(f"input data")
            self.SpeakText(f"input data")
            f = open(file, "a")
            if "data" in words:
                words = words.replace("new line", "\\n")
            if self.addSetting:
                print("adding")
                self.newVar += words.replace("data", "")
                print(self.varData)
            else:
                print("not adding")
                self.newVar = words.replace("data", "")
                print(self.varData)

            f.close()

            print(f"are you happy with the variable: \n {self.newVar} = {self.varData} (say add, restart or yes)")
            self.SpeakText(f"are you happy with the variable: \n {self.newVar} = {self.varData} (say add, restart, or yes)")

            self.currentStep = 3
        if (self.currentStep == 3):
            if "add" in words:
                self.currentStep = 1
                print("Back to step 1")
                self.SpeakText("Back to step 1")
                self.addSetting = True
                return False
            elif "restart" in words:
                self.currentStep = 1
                print("Back to step 1")
                self.SpeakText("Back to step 1")
                self.addSetting = False
                return False
            elif "yes" in words:
                f = open(file, "a")
                f.write(f"{self.newVar} = {self.varData} \n")
                f.close()
                return True
            else:
                print("Nothing found, try again")
                self.SpeakText("Nothing found, try again")


    # def advance(self, words, file):
    #     if "exit" in words:
    #         return True

    #     if "explain" in words:
    #         print(self.getFunctionalityString())
    #         self.SpeakText(self.getFunctionalityString())
    #         return False

    #     if self.currentStep == 1:       
    #         f = open(file, "a")
    #     if "data name" in words:
    #         self.data = words.replace("data type", "")
    #         f.close()

    #         self.currentStep = 2
    #     if (self.currentStep == 2):
    #         print('please give data type')
    #         if "string" in words:
    #             openbracket = words.replace("'", "")
    #         elif "array" in words:
    #             openbracket = words.replace("[", "")

    #         # hier moet een call functie komen
    #         self.currentStep = 3
    #     if (self.currentStep == 3):    
    #         print("Please give the input data")
    #         inputdata = words

    #         if openbracket.has("["):
    #             closingbracket = words.replace("]", "")
    #         else:
    #             closingbracket = words.replace("'", "")
    #         f.write(f"\n {datatype} = {openbracket} {inputdata} {closingbracket} \n")
    #     f.close()

    def getFunctionalityString(self):
        return "Step one is say 'name, then you will get a option for the name of the variable and after that you can choose data type and text input"