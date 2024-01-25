#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
 
        # sort strings
        strs = sorted(strs)

        # compare first string and last in order to find the common prefix
        first = strs[0]
        last = strs[-1]

        prefix = ""
        for i in range(len(first)):
    
            if(first[i] != last[i]):
                return prefix

            # common: add to prefix
            prefix += first[i]

        return prefix


