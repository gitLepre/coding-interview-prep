class Solution:
    def countAndSay(self, n: int) -> str:
        self.sequence = "1"
        return self.countAndSayCore(n)


    def countAndSayCore(self, n: int) -> str:
        if n == 1:
            return self.sequence
        else:
            self.sequence = self.RLE(self.sequence)
            return self.countAndSayCore(n-1)


    # RLE string compression
    def RLE(self, chars: str) -> str:
        output = ''
        if chars == "1":
            output = "11"
        else:
            # RLE algorithm
            count = 0
            char = ''
            for pos in range(len(chars)):
                s = chars[pos]
                # first pos: initialize
                if pos == 0:
                    char = s
                    count = 1
                else:
                    if s != char:
                        output = f"{output}{count}{char}"
                        char = s
                        count=1
                    else:
                        count+=1
                # last pos: add remaining chars
                if pos == len(chars)-1:
                    output = f"{output}{count}{char}"
                pos+=1
        return output


# Test
sol = Solution()
print(sol.countAndSay(4)) # 1211


