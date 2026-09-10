class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s.replace(" ", "")
        t = ""
        for i in s:
            if i.isalnum():
                t += i
        if t == t[::-1]:
            return True
        return False