def printFunction(words, file):
    f = open(file, "a")
    if "print" in words:
        printedText = words.replace("print ", "")
        print("printing")
        f.write(f"\n  print('{printedText}') \n")
    f.close()