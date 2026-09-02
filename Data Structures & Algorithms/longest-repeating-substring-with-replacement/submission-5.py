class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # get a sliding window going
        # keep a dict of freq of chars in that window
        # get the max freq out of this dict
        # replacement needed in that window is (windowSize - maxFreq)
        # shrink the window when (windowSize - maxFreq) > k
        # return max window size

        charCount = dict()
        maxLength = 0
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            # update freq of char in window
            char = s[r]
            if char not in charCount:
                charCount[char] = 0
            charCount[char] += 1

            # get max freq of char
            maxFreq = max(maxFreq, charCount[char])

            if (r - l + 1) - maxFreq > k:
                leftChar = s[l]
                # remove left char from frequency count
                charCount[leftChar] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength

            


