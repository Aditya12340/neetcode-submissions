class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen=defaultdict(int)
        for i in arr:
            seen[i]+=1
        
        ret=-1
        for i in seen.keys():
            if i==seen[i]:
                ret=max(ret,i)

        return ret
