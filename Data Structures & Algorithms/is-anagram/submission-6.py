class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t): 
            return False 
        
        for i in s: 
            if i not in seen: 
                seen[i] = 1
            else: 
                seen[i] += 1
        
        for j in t: 
            if j not in seen: 
                return False
            else: 
                seen[j] += 1
        
        counter = 0
        for value in seen.values(): 
            if value % 2 != 0: 
                counter += 1

        if counter == 0: 
            return True 
        else: 
            return False


 




        