class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        sorted_counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_counter[i][0])

        return result
        