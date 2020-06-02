class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
# # 1 solution        
        if not nums:
            return 0
        
        diff = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[diff] = nums[i]
                diff += 1
        return diff
        
    
    
    # solution # 2
        
        # l = len(nums)
        # v = 0
        # for i in range(l):
        #     if nums[i-v] == val:
        #         nums.pop(i-v)
        #         v += 1
        # return len(nums)
        