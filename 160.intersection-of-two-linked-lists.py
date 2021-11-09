#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Optimal
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

        # first
        # A = headA
        # B = headB
        # LoopA = LoopB = False
        # while headA and headB:
        #     if headA == headB:
        #         return headA
        #     headA = headA.next
        #     headB = headB.next
        #     if not headA and not LoopA:
        #         headA = B
        #         LoopA = True
        #     if not headB and not LoopB:
        #         headB = A
        #         LoopB = True

        # return


# @lc code=end
