class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        left = 1
        right = max(piles) # max pile size to finish in an hour

        answer = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                answer = k
                right = k - 1
            else:
                left = k + 1

        return answer
        