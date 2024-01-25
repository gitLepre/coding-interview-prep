# https://leetcode.com/problems/roman-to-integer/submissions/1150077362/

class Solution:
    def romanToInt(self, s: str) -> int:

        # hashmap with values
        romans = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        total = 0
        for i in range(len(s)-1):
            
            #  prev >= next : sum it!
            if(romans[s[i]] >= romans[s[i+1]]):
                # sum s[i]
                total += romans[s[i]]
                
            # prev < next : sub it!
            else:
                # sum -s[i]
                total -= romans[s[i]]

        total += romans[s[-1]]
        return total
        