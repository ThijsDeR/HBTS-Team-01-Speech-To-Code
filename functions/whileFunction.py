import functions.baseFunction as baseFunction
from voiceFunctions import voiceFunctions
from codewriter import writeLine
from wordFilter import filterWords

class whileFunctionality(voiceFunctions):
    toBePrintedText = ""
    whileType = ""
    whileType = ""
    tempValue = ""
    statements = []
    def __init__(self, spacing):
        super().__init__(5, spacing)

    def advance(self, words, file):
        if self.inlineVoiceFunction == None:
            if "exit" in words:
                return True

            if "explain" in words:
                print(self.getFunctionalityString())
                self.SpeakText(self.getFunctionalityString())
                return False
            if "done" in words:
                return True
            if "show" in words:
                print(f"statements: \n {self.statements}")
                self.SpeakText("Showing statements in console")
            if self.currentStep == 0:
                print(self.getFunctionalityString())
                self.SpeakText(self.getFunctionalityString())
                self.currentStep = 1
                return False
            elif self.currentStep == 1:
                if "while" in words:
                    self.whileType = "while"
                    print("Chose while")
                    self.SpeakText("Chose while")
                    self.currentStep = 2
                print("say the value that comes before the operator")
                self.SpeakText("say the value that comes before the operator")

            elif self.currentStep == 2:
                words = filterWords(words)
                print(f"are you happy with the first variable: \n {words} (say redo or yes)")
                self.SpeakText(f"are you happy with the first variable: \n {words} (say redo or yes)")
                self.tempValue = words
                self.currentStep = 3

            elif self.currentStep == 3:
                if "yes" in words:
                    self.statements.append({
                        "var1": self.tempValue,
                        "operator": "",
                        "var2": "",
                        "logicOperator": ""
                    })
                    print(f"added {self.tempValue} as var1")
                    self.SpeakText(f"added {self.tempValue} as var1")
                    self.currentStep = 4
                    print("say the value that becomes the operator")
                    self.SpeakText("say the value that becomes the operator")
                    return False
                elif "redo" in words:
                    self.currentStep = 2
                    print("Back to step 2")
                    self.SpeakText("Back to step 2")
                    return False

            elif self.currentStep == 4:
                words = filterWords(words)
                print(f"are you happy with the operator: \n {words} (say redo or yes)")
                self.SpeakText(f"are you happy with the operator: \n {words} (say redo or yes)")
                self.tempValue = words
                self.currentStep = 5
                
            elif self.currentStep == 5:
                if "yes" in words:
                    self.statements[len(self.statements) - 1]['operator'] = self.tempValue
                    print(f"added {self.tempValue} as operator")
                    self.SpeakText(f"added {self.tempValue} as operator")
                    self.currentStep = 6
                    print("say the value that comes after the operator")
                    self.SpeakText("say the value that comes after the operator")
                    return False
                elif "redo" in words:
                    self.currentStep = 4
                    print("Back to step 4")
                    self.SpeakText("Back to step 4")
                    return False
                print('lol')
            elif self.currentStep == 6:
                words = filterWords(words)
                print(f"are you happy with the second variable: \n {words} (say redo or yes)")
                self.SpeakText(f"are you happy with the second variable: \n {words} (say redo or yes)")
                self.tempValue = words
                self.currentStep = 7

            elif self.currentStep == 7:
                if "yes" in words:
                    self.statements[len(self.statements) - 1]['var2'] = self.tempValue
                    print(f"added {self.tempValue} as var2")
                    self.SpeakText(f"added {self.tempValue} as var2")
                    self.currentStep = 8
                    print("are you happy with the while statement? say show to show the while statement (then reply with `yes`, `no`, `add and` or `add or`)")
                    self.SpeakText("are you happy with the while statement? say show to show the while statement (then reply with `yes`, `no`, `add and` or `add or`)")
                    return False
                elif "redo" in words:
                    self.currentStep = 6
                    print("Back to step 6")
                    self.SpeakText("Back to step 6")
                    return False
            elif self.currentStep == 8:
                if "yes" in words:
                    statementString = ""
                    for index, statement in enumerate(self.statements):
                        statementString += f"{statement['var1']} {statement['operator']} {statement['var2']}"
                        if (index != len(self.statements)):
                            statementString += f"{statement['logicOperator']} "
                    if self.whileType != "else":
                        line = writeLine('text.py', f"{self.whileType} {statementString}:\n", self.spacing)
                    else:
                        line = writeLine('text.py', f"else:\n", self.spacing)
                    print(f"wrote `{line}` to the code")
                    self.SpeakText(f"wrote `{line}` to the code")
                    print(f"going into new base function")
                    self.SpeakText(f"going into new base function")
                    print(self.inlineVoiceFunction)
                    self.inlineVoiceFunction = baseFunction.BaseFunction(self.spacing + 2)
                    print(self.inlineVoiceFunction)
                    return True
                elif "no" in words:
                    self.currentStep = 1
                    self.statements.pop(len(self.statements) - 1)
                    print("Back to step 1")
                    self.SpeakText("Back to step 1")
                    return False
                elif "add and" in words:
                    self.statements[len(self.statements) - 1]['logicOperator'] = "&&"
                    self.currentStep = 2
                    return False
                elif "add or" in words:
                    self.statements[len(self.statements) - 1]['logicOperator'] = "||"
                    self.currentStep = 2
                    return False
            else:
                done = self.inlineVoiceFunction.advance(words, file)
                if done:
                    self.inlineVoiceFunction = None
                
    def getFunctionalityString(self):
        return "Step 1 is say 'while'.\n Step 2 is say a variable 1, like [name].\n Step 3 is say operator. \n Step 4 is say variable 2, like [20]\n Step 5 is say done or another statement."