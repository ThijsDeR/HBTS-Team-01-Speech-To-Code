def filterWords(words):
    filterWords = [
        {"stringTo": ">=", "stringFrom": ["greater and equal", "greater and equals", "greater equal", "greater equals"]},
        {"stringTo": "!=", "stringFrom": ["not equal", "not equals", "not equaling"]},
        {"stringTo": "==", "stringFrom": ["equal", "equals", "equaling"]},
        {"stringTo": ">", "stringFrom": ["greater than", "greater then", "grater than", "grater then", "greater ten", "grater ten"]},
        {"stringTo": "<=", "stringFrom": ["less and equal", "less and equals", "less equal", "less equals"]},
        {"stringTo": "<", "stringFrom": ["less than", "less then", "lass then", "lass than", "less ten", "lass ten"]},
        {"stringTo": "\n", "stringFrom": ["new line", "new lime"]},
    ]