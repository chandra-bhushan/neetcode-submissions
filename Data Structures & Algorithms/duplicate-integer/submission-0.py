class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = collections.defaultdict(int)

        for x in nums:
            if counts[x] > 0:
                return True

            counts[x] += 1

        return False


        