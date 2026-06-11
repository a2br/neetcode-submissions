class Solution:
    ALPHABET = list(map(chr, range(ord('a'), ord('z') + 1)))
    def hashStr(self, s):
        return tuple([s.count(c) for c in self.ALPHABET])
    def sameHash(g, h):
        return g == h

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = {}
        for s in strs:
            h = self.hashStr(s)
            if not h in indices:
                indices[h] = []
            indices[h] += [s]
        return list(indices.values())
