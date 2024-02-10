def strStr(self, haystack: str, needle: str) -> int:
    result = -1
    
    start = 0
    index = 0

    stop = False
    while(not stop):


        # needle in haystack!
        if index == len(needle):
            return start

        # overflow case
        if (start + index) == len(haystack):
            return result

        # check needle char with haystack char
        if(haystack[start + index] == needle[index]):
            index+=1
        else:
            index=0
            start+=1
        
    return result