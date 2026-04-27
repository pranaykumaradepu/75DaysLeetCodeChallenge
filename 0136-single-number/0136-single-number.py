class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Start our result at 0
        result = 0
        
        for number in nums:
            # XOR the current number with our running result
            result = result ^ number
            
        return result