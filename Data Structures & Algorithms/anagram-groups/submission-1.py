class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        end = []
        for str in strs:
            hash_key = tuple(sorted(str))
            hash_map[hash_key].append(str)
        for abc in hash_map.values():
            end.append(abc)
        return end

        