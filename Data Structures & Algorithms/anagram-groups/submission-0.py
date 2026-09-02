import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)

        for item in strs:
            sorted_item = tuple(sorted(item))
            anagram_map[sorted_item].append(item)
        
        result_list = list()
        for s in anagram_map.values():
            result_list.append(s)
        
        return result_list