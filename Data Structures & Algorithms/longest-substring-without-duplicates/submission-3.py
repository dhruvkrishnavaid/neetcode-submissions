class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        c = set()
        start = 0
        l = 0
        
        for end in range(len(s)):
            while s[end] in c:
                c.remove(s[start])
                start += 1
                
            c.add(s[end])
            l = max(l, end - start + 1)
            
        return l