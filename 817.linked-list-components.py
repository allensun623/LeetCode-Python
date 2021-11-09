#
# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # n = 0
        # while head:
        #     head = head.next
        #     n += 1
        # zeros = [0] * n
        # for i in nums:
        #     zeros[i] = i
        # if zeros == nums:
        #     return 1
        # res = 0
        # while n >= 0:
        #     if zeros[-n] != 0 and zeros[-n] + 1 != zeros[-n+1]:
        #         res += 1
        #     n -= 1
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if nums[i-1] + 1 != nums[i]:
                res += 1
        return res

        # first
        # seen = []
        # n = 0
        # while head:
        #     if head.val in nums:
        #         seen.append(n)
        #     n += 1
        #     head = head.next
        # res = 0
        # for i in range(len(seen)):
        #     if seen[i-1] + 1 != seen[i]:
        #         res += 1
        # return res


# @lc code=end
