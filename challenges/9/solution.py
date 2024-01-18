# https://leetcode.com/problems/palindrome-number/submissions/1150075600/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if negative return false
        if x < 0:
            return False
        
        # cast to string
        x = str(x)

        for pos in range( int( len(x) / 2 ) ):

            # compare first and last, and so on
            if( x[pos] != x[-1 -pos] ):
                return False

        # if it's here, it's a palindrome
        return True


        