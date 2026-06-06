class Solution:
    def sameHash(self, s, t):
        return s == t

    def hashWord(self, r: str):
        counts = defaultdict(int)
        for c in r:
            counts[c] += 1
        return counts


    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = self.hashWord(s)
        hash_t = self.hashWord(t)

        return self.sameHash(hash_s, hash_t)
