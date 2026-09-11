class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        k = prices[0]
        for i in prices[1:]:
            if k > i:
                k = i
            elif i - k > mp:
                mp = i - k
        return mp
            