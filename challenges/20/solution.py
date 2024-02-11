
def isValid(self, s: str) -> bool:
    stack = []

    # push open brackets
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            
            # avoid lonely closed brackets 
            if stack:
                open = stack.pop(-1)
            else:
                return False
            # check close brackets
            if c is ')' and open is '(' or \
                c is ']' and open is '[' or \
                c is '}' and open is '{':
                continue
            else:
                return False
    
    # avoid lonely open brackets
    if stack:
        return False
    return True
                
