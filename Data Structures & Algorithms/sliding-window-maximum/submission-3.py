class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        num_len = len(nums)
        if k >= num_len:
            return [max(nums)]

        
        for i in range(len(nums)):
            if i + k > num_len:
                break
            cur_window = nums[i: i+k]
            result.append(max(cur_window))

        return result


        