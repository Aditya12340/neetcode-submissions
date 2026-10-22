class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen = {}
        ans = []
        comp = set(arr)

        for i in range(len(arr)): 
            if arr[i] not in seen: 
                seen[arr[i]] = 1
            else: 
                seen[arr[i]] += 1 
        
        for key, value in seen.items(): 
            if key == value: 
                ans.append(value)
                
        if len(ans) == 0: 
            return -1
        else:
            return max(ans)
