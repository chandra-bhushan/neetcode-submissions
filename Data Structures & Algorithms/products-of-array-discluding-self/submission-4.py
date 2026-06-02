class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix = 1
        postfix = 1

        # [1, 2, 4, 6]
        for i, x in enumerate(nums):
            output[i] = prefix
            prefix = prefix * x

        # output = [1,1,2,8]

        for i in range(len(nums), 0, -1):
            output[i-1] = postfix * output[i-1]
            postfix = nums[i-1] * postfix

        # output = [48,24,12,8]
            

        return output