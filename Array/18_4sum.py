class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        
        
        """
        My Second solution
        """
        l_nums = len(nums)
        if l_nums < 4:
            return
        
        results = []
        nums.sort()
        a = 0 
        for a, n1 in enumerate(nums[:l_nums-3]):
            if 4 * n1 > target or nums[:-1] < target:
                break
            if a > 0 and nums[a-1] == nums[a]:
                continue
                
            # number b   
            for i, n2 in enumerate(nums[a+1:l_nums-2]):
                b = a + i + 1
                if 3 * n1 + n2 > target:
                    break
                if i > 0 and nums[b-1] == nums[b]:
                    continue
                
            # number c & d  
                c = b + 1
                d = l_nums - 1
                while c < d:
                    n3 = nums[c]
                    n4 = nums[d]
                    total = n1 + n2 + n3 + n4
                    
                    if total == target:
                        results.append([n1, n2, n3, n4])
                        while c + 1 < d and nums[c] == nums[c+1]:
                            c += 1
                        while c + 1 < d and nums[d] == nums[d-1]:
                            d -= 1
                            
                    if total < target:
                        c += 1

                    else:
                        d -= 1
                        
        return results
                    
                    
        """
        My first solution
        """
#         l_nums = len(nums)
#         if l_nums < 4:
#             return
        
#         results = []
#         nums.sort()
#         a = 0 
#         while a < l_nums - 3:
#             b = a + 1
#             while b < l_nums - 2:
#                 c = b + 1
#                 d = l_nums - 1
#                 while c < d:
#                     n1 = nums[a]
#                     n2 = nums[b]
#                     n3 = nums[c]
#                     n4 = nums[d]
#                     total = n1 + n2 + n3 + n4
#                     # print("===================================")
#                     # print(nums)
#                     # print("a:{} b:{} c:{} d:{}".format(a, b, c, d))
#                     # print("total: {} = {} + {} + {} + {}".format(total, n1, n2, n3, n4))
                    
#                     if total == target:
#                         results.append([n1, n2, n3, n4])
#                         while c + 1 < d and nums[c] == nums[c+1]:
#                             c += 1
#                         while c + 1 < d and nums[d] == nums[d-1]:
#                             d -= 1
                            
#                     if total < target:
#                         c += 1

#                     else:
#                         d -= 1
                        
#                 b += 1
#                 while b < l_nums - 2 and nums[b-1] == nums[b]:
#                     b += 1
                    
#             a += 1
#             while a < l_nums - 3 and nums[a-1] == nums[a]:
#                 a += 1
                        
#         return results
                    
                