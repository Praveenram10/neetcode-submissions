class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        same = ""
        for i in zip(*strs):
            if len(set(i))==1:
                same += i[0]
            else:
                break
        return same
        