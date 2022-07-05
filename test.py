# Python program to translate
# speech to text and text to speech


import importlib
import speech_recognition as sr
import pyttsx3
import os
import text
import functions.print as printFunction
import functions.ifFunction as ifFunction
import functions.whileFunction as whileFunction
import functions.datatypes as dataFunction

# Initialize the recognizer
r = sr.Recognizer()
os.remove('text.py')
f = open("text.py", "w")
f.write("def voiceCommand():\n print('') \n")
f.close()
print('ready')
voiceFunction = None

# Function to convert text to
# speech
def SpeakText(command):
  
  # Initialize the engine
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()
  
  
# Loop infinitely for user to
# speak

while(1):

  
  # Exception handling to handle
  # exceptions at the runtime
  try:
    
    # use the microphone as source for input.
    with sr.Microphone() as source2:
      # wait for a second to let the recognizer
      # adjust the energy threshold based on
      # the surrounding noise level
      r.adjust_for_ambient_noise(source2, duration=0.2)
      
      #listens for the user's input
      audio2 = r.listen(source2)
      
      # Using google to recognize audio
      MyText = r.recognize_google(audio2)
      MyText = MyText.lower()
      print(f"heard: {MyText}")
      if voiceFunction != None:
        done = voiceFunction.advance(MyText, "text.py")
        if done:
          voiceFunction = None
      else:
        if "make" in MyText:
          if "print" in MyText:
            voiceFunction = printFunction.printFunctionality()
            print(voiceFunction.getFunctionalityString())
            SpeakText(voiceFunction.getFunctionalityString())

          if "data" in MyText:
            voiceFunction = dataFunction.dataFunctionality()
            print(voiceFunction.getFunctionalityString())
            SpeakText(voiceFunction.getFunctionalityString())

        elif "while" in MyText:
            voiceFunction = whileFunction.whileFunctionality()
            print(voiceFunction.getFunctionalityString())
            SpeakText(voiceFunction.getFunctionalityString())

        elif "execute" in MyText:
          importlib.reload(text)
          text.voiceCommand()
        elif "reset" in MyText:
          os.remove('text.py')
          f = open("text.py", "w")
          f.write("def voiceCommand():\n print('') \n")
          f.close()
          print("Resetted all code")
          SpeakText("Resetted all code")
        elif "help" in MyText:
          print("Available functions: \n - make (print)\n - execute\n - reset\n - help")
          SpeakText("Available functions: \n - make (print)\n - execute\n - reset\n - help")
        else:
          print(f"Nothing found for {MyText}")
          SpeakText(f"Nothing found for {MyText}")
  
  except sr.RequestError as e:
    print(f"Nothing found, try help")
    SpeakText(f"Nothing found, try help")
    # print("Could not request results; {0}".format(e))
    
  except sr.UnknownValueError:
    print(f"Nothing found, try help")
    SpeakText(f"Nothing found, try help")
    # print("unknown error occured")