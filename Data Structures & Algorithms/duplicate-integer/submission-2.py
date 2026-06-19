class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        num_len = len(nums)
        
        seen = {
            nums[0]: True
        }
        for i in range(1, num_len):
            if nums[i] in seen:
                return True
            seen[nums[i]] = True
        
        return False