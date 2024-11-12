class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize two pointers at the beginning and end of the array
        left = 0
        right = len(height) - 1
        
        # Initialize the maximum area to zero
        max_area = 0
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the height of the current container, which is the shorter of the two lines
            current_height = min(height[left], height[right])
            # Calculate the width of the container, which is the distance between the two lines
            width = right - left
            # Calculate the area and update max_area if this area is greater
            current_area = current_height * width
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward, as it limits the height of the container
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area