def printFunction(words, file):
    f = open(file, "a")
    if "for" in words:
        print("please give for-operator")
        var1 = words.replace("for", "")
        if "index" in words:
              forloopindex = words.replace("i")
        elif "equals" in words:
             equals = words.replace("let i ")
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
            
        print("printing")
        f.write(f"\n  '{var1}( let {forloopindex} {equals} {forloopnumber}; {forloopindex} {operator} array.length; {forloopindex}{addorless}) '; \n")
    f.close()
#     for (let index = 0; index < array.length; index++) {
#     const element = array[index];
# }