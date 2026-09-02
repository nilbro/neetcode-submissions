class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        res = [1] * len(nums)

        # populate prefix
        for i in range(1, len(nums)):
            prefix[i]=prefix[i-1] * nums[i-1]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            print(post)
            print(res)
            res[i] = post * prefix[i]
            post = post * nums[i] 
        return res




        
        
        