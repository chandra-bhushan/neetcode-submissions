class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0
        n_start, n_end = newInterval

        while i < n and intervals[i][1] < n_start:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= n_end:
            n_start = min(n_start, intervals[i][0])
            n_end = max(n_end, intervals[i][1])
            i += 1

        result.append([n_start, n_end])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result