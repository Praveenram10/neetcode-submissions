from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_map = defaultdict(list)

        for i in strs:
            sorted_key = tuple(sorted(i))
            anagram_map[sorted_key].append(i)
        for values in anagram_map.values():
            result.append(values)
        return result
        