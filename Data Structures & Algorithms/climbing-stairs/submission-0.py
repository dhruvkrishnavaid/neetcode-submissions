class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n <= 2:
            return n
        
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
            
        return b