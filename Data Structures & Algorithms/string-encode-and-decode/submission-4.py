class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for item in strs:
            len_item = len(item)
            encoded += str(len_item) + "#" + item
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j = j+1
            str_len = int(s[i:j])
            decoded.append(s[j+1 : j + str_len + 1])
            i = j + str_len + 1
        return decoded


