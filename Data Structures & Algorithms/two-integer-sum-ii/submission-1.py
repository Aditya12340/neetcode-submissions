class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        n = len(numbers)

        for i in range(n): 
            need = target - numbers[i]

            if need not in seen: 
                seen[numbers[i]] = i 
            else: 
                x = seen.get(need)
                x += 1
                return [x , i+1]        