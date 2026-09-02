import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()
        prod = math.prod(nums)
        for i in range(0, len(nums)):
            x = nums[:i] + nums[i+1:]
            res.append(math.prod(x))
        return res

        