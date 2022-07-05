import pyttsx3

class voiceFunctions:
    stepAmountMax = 1
    currentStep = 1
    
    def __init__(self, stepAmount):
        self.stepAmountMax = stepAmount

    def SpeakText(self, command):
  
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    