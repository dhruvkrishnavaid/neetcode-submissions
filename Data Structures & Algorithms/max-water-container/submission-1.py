class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mv = 0
        while l < r:
            v = (r - l) * min(heights[l], heights[r])
            if v > mv:
                mv = v
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mv