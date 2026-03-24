class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            current_area = h * w
            
            if current_area > max_area:
                max_area = current_area
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area