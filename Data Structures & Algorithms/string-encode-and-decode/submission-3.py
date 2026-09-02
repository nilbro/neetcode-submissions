class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_dict = dict()
        for i in range(0, len(strs)):
            encoded_dict[i] = strs[i]
        return str(encoded_dict)

    def decode(self, s: str) -> List[str]:
        strs = list()
        for k, v in ast.literal_eval(s).items():
            strs.append(v)
        return strs
        

