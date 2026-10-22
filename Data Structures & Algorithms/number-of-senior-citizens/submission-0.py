class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for i in details: 
            age = int(i[11]) * 10 + int(i[12])
            if age > 60: 
                counter += 1
            age = 0
        
        return counter