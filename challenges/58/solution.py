def lengthOfLastWord(s: str) -> int:

    # length of the initial word (starting from the end of the string)
    start = len(s)

    started = False
    for pos in range(len(s)-1, 0, -1):

        c = s[pos]
        
        # starting position
        if c is not " ":
            if not started:
                start = pos
                started = True
                continue

        if started:
            if c is " ":
                return start-pos

    return start+1