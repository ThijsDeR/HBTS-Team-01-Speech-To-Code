def filterWords(words):
    filterWords = [
        {"stringTo": ">=", "stringFrom": ["greater equals", "greater and equals", "greater and equal", "greater equal", ]},
        {"stringTo": "!=", "stringFrom": ["not equals", "not equal", "not equaling"]},
        {"stringTo": "==", "stringFrom": ["equals", "equal" , "equaling"]},
        {"stringTo": ">", "stringFrom": ["greater than", "greater then", "grater than", "grater then", "greater ten", "grater ten"]},
        {"stringTo": "<=", "stringFrom": ["less and equals","less equals", "less and equal", "less equal"]},
        {"stringTo": "<", "stringFrom": ["less than", "less then", "lass then", "lass than", "less ten", "lass ten"]},
        
        {"stringTo": "\n", "stringFrom": ["new line", "new lime"]},
        
        {"stringTo": "//", "stringFrom": ["floor division", "floor divide"]},
        {"stringTo": "+=", "stringFrom": ["plus equals", "plus equal"]},
        {"stringTo": "-=", "stringFrom": ["minus equals", "minus equal"]},
        {"stringTo": "*=", "stringFrom": ["times equals", "times equal"]},
        {"stringTo": "/=", "stringFrom": ["divide equals", "divide equal"]},
        {"stringTo": "%=", "stringFrom": ["modules equals", "modules equal"]},
        {"stringTo": "**=", "stringFrom": ["times times equals", "exponentiation equals", "exponenent equals", "times times equal", "exponentiation equal", "exponenent equal"]},
        {"stringTo": "&=", "stringFrom": ["and equals", "and sign equals", "and equal", "and sign equal"]},
        {"stringTo": "|=", "stringFrom": ["or equals", "or equal", "or sign equals", "or sign equal"]},
        
        {"stringTo": "/", "stringFrom": ["divides", "divides by", "divide", "divide by", "divided"]},
        {"stringTo": "%", "stringFrom": ["modulo", "modulus"]},
        
        
        {"stringTo": "++", "stringFrom": ["double plus", "double addition", "double add", "plus plus", "addition addition", "add add"]},
        {"stringTo": "--", "stringFrom": ["double minus", "double subtract", "double subtraction", "minus minus", "subtract subtract", "subtraction subtraction"]},
        {"stringTo": "**", "stringFrom": ["double times", "double multiplication", "times times", "multiplication multiplication", "exponentation", "exponent"]},
        
        {"stringTo": "+", "stringFrom": ["plus", "addition", "add"]},
        {"stringTo": "-", "stringFrom": ["minus", "subtract", "subtraction"]},
        {"stringTo": "*", "stringFrom": ["times", "multiplication"]},    
    ]

    for wordDict in filterWords:
        for stringFrom in wordDict['stringFrom']:
            words = words.replace(stringFrom, wordDict['stringTo'])

    return words