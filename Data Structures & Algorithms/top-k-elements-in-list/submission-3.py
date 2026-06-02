class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]

        # nums = [1,2,2,3,3,3], k = 2 # output [2,3]
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # counter = {1: 2, 2: 3, 3: 4}
        
        for num, count in counter.items():
            freq[count].append(num)

        # freq = [[], [], [1], [2], [3], [], [], [], []]
        
        result = []
        # freq is already sorted from last index
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

                if len(result) == k:
                    return result

        return result
        