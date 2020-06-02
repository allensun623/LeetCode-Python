class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        Optimal solution
        """
#         result, diff = 0, sys.maxint
#         nums.sort()

#         for i in xrange(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             left, right = i + 1, len(nums) - 1

#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]
#                 hold_diff = abs (total - target)

#                 if not hold_diff:
#                     return total

#                 if hold_diff  < diff:
#                     result = total
#                     diff = hold_diff

#                 if total < target:
#                     left += 1

#                 else:
#                     right -= 1

#         return result
        
        
        
        """
        My first solution
        """
        if len(nums) < 3:
            return None
        
        nums.sort()
        l_nums = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        closest_diff = abs(closest - target)
        
        for i, n1 in enumerate(nums[:l_nums-2]):
            j = i + 1
            k = l_nums - 1
            while j < k:
                n2 = nums[j]
                n3 = nums[k]
                total = n1 + n2 + n3

                if total == target:
                    return total

                diff = abs(total - target)
                if diff < closest_diff:
                    closest = total
                    closest_diff = diff

                # left pointer moves
                if total < target:
                    j += 1
                    
                # right pointer moves
                else:
                    k -= 1

        return closest
                
                
            
        
