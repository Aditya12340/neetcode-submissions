class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        d1 = {}
        for ch in s1:
            if ch not in d1:
                d1[ch] = 1
            else:
                d1[ch] += 1       
        for i in range(n2 - n1 + 1):
            window = {}            
            for j in range(n1):
                ch = s2[i + j]
                if ch not in window:
                    window[ch] = 1
                else:
                    window[ch] += 1
            if window == d1:        
                return True
        return False                