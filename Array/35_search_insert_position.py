class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        Binary
        """
        
        
        left = 0
        right = len(nums) - 1
        if nums[right] < target:
            return right + 1
        if nums[left] > target:
            return left
        
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif left + 1 == right:
                return mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid

        return left
        
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) / 2
#             if nums[mid] >= target:
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         return left
        
        """
        My first solution
        """
#         for i, x in enumerate(nums):
#             if x >= target:
#                 return i
        
#         return len(nums)

