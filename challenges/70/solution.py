# solving for case n=2,3,4,5.. we note that is a fibonacci sequence
def climbStairs(self, n: int) -> int:
    a = 0
    b = 1
    for step in range(n):
        f_b = b
        b = a+b
        a = f_b
        
    return b        