#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
  def longestPalindrome(self, s: str) -> int:
    # Second
    chs = [0] * 52
    for c in s:
      chs[ord(c) - ord('a')] += 1
    odds = sum([v % 2 for v in chs])
    # res = len(s) - odds + (odds >= 1)
    return len(s) - odds + bool(odds)
    # First
    # dic = {}
    # for c in s:
    #   dic[c] = dic.get(c, 0) + 1
    # odds = sum([v % 2 for v in dic.values()])
    # res = len(s) - odds + (odds >= 1)
    # return res

    # @lc code=end
