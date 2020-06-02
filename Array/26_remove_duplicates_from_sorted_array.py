class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        new_tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = nums[i]
        return new_tail+1

#         A = nums
#         if not A:
#             return 0

#         newTail = 0

#         for i in range(1, len(A)):
#             if A[i] != A[newTail]:
#                 newTail += 1
#                 A[newTail] = A[i]

#         return newTail + 1