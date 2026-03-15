class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        full_set = set(range(1,n+1))

        actual_set = set(nums)

        return list(full_set - actual_set)

