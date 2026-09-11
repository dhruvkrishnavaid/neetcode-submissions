class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(1, len(prices)):
            s = prices[i]
            b = min(prices[:i])
            w = s - b
            if p < w:
                p = w
        return p