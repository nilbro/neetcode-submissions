class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_len = len(s1)
        s2_len = len(s2)

        while l <= s2_len - s1_len:
            sub = s2[l:l + s1_len]
            if sorted(sub) == sorted(s1):
                return True
            l += 1

        return False
