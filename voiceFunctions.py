import pyttsx3

class voiceFunctions:
    stepAmountMax = None
    currentStep = 0
    inlineVoiceFunction = None
    spacing = None
    
    def __init__(self, stepAmount, spacing):
        self.stepAmountMax = stepAmount
        self.spacing = spacing

    def SpeakText(self, command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()