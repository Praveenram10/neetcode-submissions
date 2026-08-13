class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
        """
        ab = set()
        for num in nums:
            if num in ab:
                return True
            ab.add(num)
        return False