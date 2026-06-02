class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(list(set(nums)))        
        # use sliding window to find the max consecuting

        left = 0
        num_len = len(sorted_nums)
        max_consecutive = 1
        i = 1
        print(sorted_nums)
        for i in range(1, num_len):
            if (sorted_nums[i] - sorted_nums[i - 1]) == 1:
                max_consecutive = max(max_consecutive, i - left + 1)
            else:
                left = i            

        return max_consecutive
            

        