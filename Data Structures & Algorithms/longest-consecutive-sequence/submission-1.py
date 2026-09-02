class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = sorted(set(nums))
        print(nums_set)
        max_count = 0
        count = 0
        for i in range(0, len(nums_set)-1):
            if nums_set[i+1] - nums_set[i] == 1:
                count+=1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count +1
        