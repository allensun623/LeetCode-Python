class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for i, num in enumerate(nums):
            s = target - num
            if s in seen:
                return [seen[s], i]
            else:
                seen[num] = i
    