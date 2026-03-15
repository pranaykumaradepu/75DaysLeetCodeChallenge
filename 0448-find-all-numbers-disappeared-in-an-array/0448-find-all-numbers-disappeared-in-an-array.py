class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        actual_set = set(nums)
        n = len(nums)
        
        return [i for i in range(1, n + 1) if i not in actual_set]

