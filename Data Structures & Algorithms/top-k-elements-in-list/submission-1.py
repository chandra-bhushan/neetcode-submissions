from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_count = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(sorted_count[i][0])

        return output
        