class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = collections.defaultdict(int) # store bt key num
        for x in nums:
            if x in counter:
                return True # found a duplicate
            
            counter[x] += 1 # store in dict by key
        
        return False
        