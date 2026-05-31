class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            second = target - num
            
            if second in seen:
                return [seen[second], index]

            seen[num] = index

        return [0,0]

            

        