def ifFunction(words, file):
    f = open(file, "a")
    if "if" in words:
        print("Please give the first variable:")
        variable1 = words.replace("if", "")

        print("Please give the operator:")
        if "equals" in words:
            operator = words.replace("==")
        elif "not equals" in words:
            operator = words.replace("!=")
        elif "less than" in words:
            operator = words.replace("<")
        elif "less than or equals to" in words:
            operator = words.replace("<=")
        elif "greater than" in words:
            operator = words.replace(">")
        elif "greater than or equals to" in words:
            operator = words.replace("=>")
            
        print("Please give the second variable:")
        variable2 = words.replace("")
        f.write(f"\n if('{variable1} + {operator} + {variable2}') \n") 
    f.close()