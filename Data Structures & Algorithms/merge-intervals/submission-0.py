class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals)
        merged = [intervals[0]]
        for start, end in intervals[1: ]:
            last_start, last_end = merged[-1]
            if last_start <= start <= last_end:
                end = max(end, last_end)
                merged[-1] = [last_start, end] # replace last
            else:
                merged.append([start, end])
        
        return merged



        