class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        elif len(nums) == 3 and sum(nums) != 0:
            return []
        final = []
        for i in range(len(nums)):
            target = -nums[i]
            temp_arr = sorted(nums[i+1:])
            l, r = 0, len(temp_arr)-1
            while r > l:
                total = temp_arr[l] + temp_arr[r]
                if total == target:
                    triplet = [-target, temp_arr[l], temp_arr[r]]
                    if sorted(triplet) not in final:
                        final.append(sorted(triplet))
                    r = r-1
                    l = l+1
                if total > target:
                    r = r-1
                if total < target:
                    l = l+1
        return final
