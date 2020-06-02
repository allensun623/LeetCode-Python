class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """ 
        1. solution
        """
        sol = list()
        nums.sort()
        l_nums = len(nums)
        for i, n1 in enumerate(nums[:l_nums-2]):
            if n1 > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = l_nums - 1

            while l < r :
                n2 = nums[l]
                n3 = nums[r]
                total = n1 + n2 + n3
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    sol.append([n1, n2 ,n3])
                    while l<r and nums[l]==nums[l+1]: 
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                    
                    
        return sol
                    
            
            
    
        """
        solution # 2
        """             
#         sol = list()
#         nums.sort()
#         l_nums = len(nums)
#         for i, x in enumerate(nums[:l_nums-2]):
#             if x > 0:
#                 break
#             for j, y in enumerate(nums[i+1:l_nums-1]):
#                 if -(x+y) in nums[i+j+2:]:
#                     new_nums = [x, y, -(x+y)]
#                     if new_nums not in sol:
#                         sol.append(new_nums)
                    
#         return sol
        
        
        """
        solution # 3
        """ 
#         # check two sum
#         def two_sum(two_nums, target):
#             # multiple answers
#             found = list()
#             seen = list()
#             for x in two_nums:
#                 y = target - x
#                 if y in seen:
#                     found.append([x, y])
#                 else:
#                     seen.append(x)
#             return found
        
#         # if unique list
#         def unique_list(sol, new_nums):
#             if not sol:
#                 return True
#             for list_i in sol:
#                 if set(list_i) == set(new_nums):
#                     return False
#             return True
        
        
#         sol = list()         
#         for i, x in enumerate(nums):
#             y = - x
#             target_nums = [nums[j] for j in range(len(nums)) if j != i] 
#             new_two = two_sum(target_nums, y)
#             if new_two:
#                 for new_nums in new_two:
#                     new_nums.append(x)
#                     if unique_list(sol, new_nums):
#                         sol.append(new_nums)
                    
#         return sol    
            
                