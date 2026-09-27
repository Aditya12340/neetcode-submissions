class Solution:
        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            store = {}
            st = []
            res = []

            for idx, i in enumerate(points):
                distance = i[0]**2 + i[1]**2
                store[idx] = distance
                st.append(distance)

            st = sorted(st)

            for z in range(k):
                keys = [key for key, val in store.items() if val == st[z]]
                key = keys[0]       
                res.append(points[key])
                del store[key]    

            return res