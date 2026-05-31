class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()   # stores indices
        result = []

        for i in range(len(nums)):

            window = i - k + 1
            # remove indices outside window            
            while q and q[0] < window:
                q.popleft()

            # maintain decreasing order
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # window complete
            if i >= k - 1:
                result.append(nums[q[0]])

        return result