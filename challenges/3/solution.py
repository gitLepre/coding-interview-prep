def lengthOfLongestSubstring(self, s: str) -> int:
    max = 0
    start = 0
    stop = 0
    # solve with an hashmap
    letters = {}
    
    # move over each character of the string
    for i in range(len(s)):

        c = s[i]

        # repeated char
        if(c in letters):
            if letters[c]+1 > start:
                start = letters[c]+1
        
        letters[c] = i
        stop = i+1
        
        if (stop - start > max):
            max = stop - start
        
    return max