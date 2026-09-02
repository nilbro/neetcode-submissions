class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_set = len(set(nums))
        len_nums = len(nums)
        if len_set < len_nums:
            return True
        return False