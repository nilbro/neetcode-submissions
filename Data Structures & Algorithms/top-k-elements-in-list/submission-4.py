from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_top_occurences = Counter(nums).most_common(k)
        k_top_occurences_dict = dict(k_top_occurences)

        occurences_list = [ [] for _ in range(len(nums)+1) ]

        for k, v in k_top_occurences_dict.items():
            occurences_list[v].append(k)
        
        result_list = []
        for i in range(len(occurences_list)-1,0,-1):
            for j in occurences_list[i]:
                result_list.append(j)
        
        return result_list

