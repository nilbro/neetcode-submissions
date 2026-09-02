class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        res = 0
        temp = []
        while i < n:
            if s[i] not in temp:
                temp.append(s[i])
                res = max(res, len(temp))
            else:
                # Remove characters from the start until s[i] is gone
                while s[i] in temp:
                    temp.pop(0)
                temp.append(s[i])
            i += 1
        return res
