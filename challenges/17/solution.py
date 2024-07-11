def letterCombinations(digits: str):

    # helper function
    def cartesian_product(list1: list, list2: list):
        res = []
        for word in list1:
            for letter in list2:
                res.append(word+letter)
        return res
    
    # check empty string
    result = []
    if len(digits) < 1:
        return result

    keyboard = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    # first digit
    result = keyboard[digits[0]]
    # all the other digits
    for i in range(1, len(digits)):
        result = cartesian_product(result, keyboard[digits[i]] )

    return result
    

