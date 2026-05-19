class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        dig2 = []
        for i in range(len(digits)): 
            num += (digits[i] * (10**(len(digits)- i - 1)))
            print(num)
        num += 1
        num_str = str(num)
        len2 = len(num_str)

        for j in range(len2):
            dig2.append(num_str[j])
        
        return dig2


        
            
        