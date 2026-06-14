class Solution:

    def encode(self, strs: List[str]) -> str:
        # length,i1,i2/joined
        res = []
        for s in strs:
            res += [f"{len(s)}#" + s]
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            sep = s.find("#", i)
            length = int(s[i:sep])
            word = s[sep+1:sep+1+length]
            res += [word]
            i = sep + 1 + length
        return res
