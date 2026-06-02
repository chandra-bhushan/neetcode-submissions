class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if (n - 1) not in nums_set:
                mc = 0
                while True:
                    if (n + mc) in nums_set:
                        mc +=1
                    else:
                        break 

                longest = max(longest, mc)
        return longest
            

        