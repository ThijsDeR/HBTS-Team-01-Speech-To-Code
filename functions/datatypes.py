def dataFunction(words, file):
    f = open(file, "a")
    if "data type" in words:
        if "string" in words:
            printedText = words.replace("data type string ", "")
            print("data type = string")
            f.write(f"\n  string = '{printedText}' \n")
        elif "array" in words:
            printedText = words.replace("data type array ", "")
            print("data type = array")
            f.write(f"\n  array = [{printedText}] \n")
    f.close()