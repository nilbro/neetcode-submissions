class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while r > l:
            total = numbers[r] + numbers[l]
            print(l, r, total)
            if total == target:
                return [l+1, r+1]
            if total > target:
                r = r-1
            if total < target:
                l = l+1

