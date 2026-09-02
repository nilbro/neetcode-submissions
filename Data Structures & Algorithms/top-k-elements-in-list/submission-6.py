class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        num_count = Counter(nums)
        res = []
        i = 0
        while k > 0:
    
            res.append(num_count.most_common()[i][0])
            i+=1
            k-=1
        return res