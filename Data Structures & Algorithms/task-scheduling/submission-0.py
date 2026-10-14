from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())

        num_max = sum(
            count == max_freq
            for count in freq.values()
        )

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + num_max
        )
        
        