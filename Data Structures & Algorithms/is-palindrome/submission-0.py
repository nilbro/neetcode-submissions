
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non alphanumeric chars and compare with reverse
        clean_s = ''.join(char for char in s if char.isalnum())
        return clean_s.lower()[::-1] == clean_s.lower()