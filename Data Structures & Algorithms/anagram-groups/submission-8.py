class Solution:
    ALPHABET = list(map(chr, range(ord('a'), ord('z') + 1)))
    
    def hashStr(self, s):
        return tuple([s.count(c) for c in self.ALPHABET])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = defaultdict(list)
        for s in strs:
            h = self.hashStr(s)
            indices[h] += [s]
        return list(indices.values())
