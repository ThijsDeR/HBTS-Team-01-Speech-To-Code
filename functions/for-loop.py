def forFunction(words, file):
    f = open(file, "a")
    if "for" in words:
        print("please give operator")
        if "index" in words:
              forloopindex = words.replace("i")
        if "equals" in words:
             equals= words.replace("let i ")
        if "one" in words:
            forloopnumber =words.replace("1")
        if "zero" in words:
            forloopnumber =words.replace("0")
        if "greater than" in words:
            operator =words.replace(">")
        if "less than" in words:
            operator =words.replace("<")
        if "less than or equals to" in words:
            operator =words.replace("<=")
        if "greater than or equals to" in words:
            operator =words.replace("=>")
        if "plus" in words:
            addless =words.replace("++")
        if "minus" in words:
            addless =words.replace("--")
            
        print("printing")
        f.write(f"\n  for(' let {forloopindex} {equals} {forloopnumber}; {forloopindex} {operator} array.length; {forloopindex}{addless}) '; \n")
    f.close()
#     for (let index = 0; index < array.length; index++) {
#     const element = array[index];
    
# }