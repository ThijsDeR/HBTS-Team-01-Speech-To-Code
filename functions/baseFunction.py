import importlib
import os
from functions.datatypes import dataFunctionality
from functions.ifFunction import ifFunctionality
from functions.print import printFunctionality
from functions.whileFunction import whileFunctionality
from voiceFunctions import voiceFunctions
import text


class BaseFunction(voiceFunctions):
    def __init__(self, spacing):
        super().__init__(1, spacing)
        self.currentStep = 0
    def advance(self, words, file):
        if self.inlineVoiceFunction == None:
            if "done" in words:
                return True
            if self.currentStep == 0:
                print(self.getFunctionalityString())
                self.SpeakText(self.getFunctionalityString())
                self.currentStep = 1
            elif self.currentStep == 1:
                if "make" in words:
                    if "print" in words:
                        self.inlineVoiceFunction = printFunctionality(self.spacing)
                        print(self.inlineVoiceFunction == None)
                    elif "data" in words:
                        self.inlineVoiceFunction = dataFunctionality(self.spacing)
                    elif "while" in words:
                        self.inlineVoiceFunction = whileFunctionality(self.spacing)
                    elif "if statement" in words: 
                        self.inlineVoiceFunction = ifFunctionality(self.spacing)
                    
                elif "execute" in words:
                    importlib.reload(text)
                    text.voiceCommand()
                elif "reset" in words:
                    os.remove(file)
                    f = open(file, "w")
                    f.write("def voiceCommand():\n print('') \n")
                    f.close()
                    print("Resetted all code")
                    self.SpeakText("Resetted all code")
                elif "help" in words:
                    print("Available functions: \n - make (print)\n - execute\n - reset\n - help")
                    self.SpeakText("Available functions: \n - make (print)\n - execute\n - reset\n - help")
                else:
                    print(f"Nothing found for {words}")
                    self.SpeakText(f"Nothing found for {words}")
        if self.inlineVoiceFunction != None:
            done = self.inlineVoiceFunction.advance(words, file)
            if done:
                self.inlineVoiceFunction = None
                self.currentStep = 0
    def getFunctionalityString(self):
        return "Use the help function to hear more about the options"