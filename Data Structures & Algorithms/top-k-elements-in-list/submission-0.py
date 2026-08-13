class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for i in nums:
            hash_map[i] = hash_map[i] + 1
        return heapq.nlargest(k, hash_map.keys(), key=hash_map.get)
            
        