class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
       
        prod = self.__get_all_products(nums)
        result = []
        for i, x in enumerate(nums):
            if x == 0:
                result.append(prod)
            else:
                if zero_count > 0:
                    result.append(0)
                else:
                    result.append(prod // x)

        return result

    
    def __get_all_products(self, nums):
        prod = 1
        for x in nums:
            if x != 0:
                prod *= x

        return prod
        