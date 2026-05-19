class Solution:

    def square(self,n):
        sum1 = 0
        temp = 0
        n = str(n)
        for j in n: 
            temp = int(j)
            sum1 += temp ** 2
        return sum1

    def isHappy(self, n: int) -> bool:
        sum = 0
        res = []
        temp = 0
        temp2 = 0
        n = str(n)
        for i in n: 
            temp2 = int(i)
            sum += temp2 **2
        if sum == 1:
            return True 
        else: 
            while sum not in res: 
                res.append(sum)
                if sum == 1:
                    return True
                sum = self.square(sum)
            return False 
            

            




            
        