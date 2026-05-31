class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        
        max_consec = 1
        current = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                current += 1
            else:
                current = 1

            max_consec = max(max_consec, current)

        return max_consec





        