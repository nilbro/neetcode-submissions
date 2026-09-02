class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        n = len(nums)

        # iterate through given list
        for i in range(n):
            if i> 0 and nums[i] == nums[i-1]:
                continue # skip duplicate i 
            l, r = i+1, n-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l = l+1
                    r = r-1
                    if nums[l] == nums[l-1]:
                        l = l+1 # skip duplicate l
                    if nums[r] == nums[r+1]:
                        r = r-1 # skip duplicate l
                if total > 0:
                    r = r-1
                if total < 0:
                    l = l+1
        return result
