class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # elem: count
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        arr = []
        for n, cnt in counts.items():
            arr.append((cnt, n))
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res