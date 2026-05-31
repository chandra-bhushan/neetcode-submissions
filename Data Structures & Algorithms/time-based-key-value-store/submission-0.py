class TimeMap:

    def __init__(self):
        self.__store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.__store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.__store[key]

        left = 0
        right = len(values) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
        
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result