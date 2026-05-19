class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = []
        s = s.lower()
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace("!", "")
        s = s.replace(",", "")
        s = s.replace(":", "")
        s = s.replace(";", "")
        s = s.replace("'", "")
        s = s.replace(" "" ", "")
        s = s.replace(".", "")
        rev = s[::-1]
        if rev == s:
            return True 
        else:
            return False
        