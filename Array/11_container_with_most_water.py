class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        optimal solution
        """
        l = 0 
        r = len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        
        """
        My first solution
        """
#         l = 0
#         r = len(height) - 1
#         opt_area = (r - l) * min(height[l], height[r])

#         while l + 1 < r:
#             # left move  
#             if height[l] < height[r]:
#                 l += 1
#                 while height[l] <= height[l-1]:
#                     l += 1
#             # right move
#             else:
#                 r -= 1
#                 while height[r] <= height[r+1]:
#                     r -= 1
#             # area
#             opt_area = max((r - l) * min(height[l], height[r]), opt_area)
                
#         return opt_area
        
