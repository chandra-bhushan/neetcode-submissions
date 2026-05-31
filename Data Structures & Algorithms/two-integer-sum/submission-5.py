class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            second = target - value
            
            if second in nums:
                try:
                    second_idx = nums.index(second, index + 1)
                    return [index, second_idx]
                except ValueError:
                    pass
                

        return [0,0]

            

        