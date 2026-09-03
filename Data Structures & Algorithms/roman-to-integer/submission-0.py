class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        summ = 0
        i = 0
        while i < len(s)-1:
            if lookup.get(s[i]) < lookup.get(s[i+1]):
                summ -= lookup.get(s[i])
            else:
                summ += lookup.get(s[i])
            i+=1
        return summ+lookup.get(s[-1])