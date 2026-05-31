class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for i in range(nums_len - 1):
            first = nums[i] 
            second = target - first
            try:
                second_index = nums.index(second, i+1)
                return [i, second_index]
            except ValueError:
                continue

        return []
        