class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = list()

        # populate prefix
        for i in range(1, len(nums)):
            prefix[i]=math.prod(nums[:i])
        
        # populate postfix
        reverse_nums = list(reversed(nums))
        for i in range(1, len(nums)):
            postfix[i]= math.prod(reverse_nums[:i])
        postfix = list(reversed(postfix))

        
        for i in range(0, len(nums)):
            res.append(postfix[i] * prefix[i])
        return res



        
        
        