from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences_dict = dict(Counter(nums))
        k_top_occurences = Counter(nums).most_common(k)
        k_top_occurences_dict = dict(k_top_occurences)
        k_top_occurences_list = list()

        for k, v in k_top_occurences_dict.items():
            k_top_occurences_list.append(k)
        
        return k_top_occurences_list
        
