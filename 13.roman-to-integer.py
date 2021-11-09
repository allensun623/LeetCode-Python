#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = roman[s[0]]
        for i in range(1, len(s)):
            if roman[s[i-1]] < roman[s[i]]:
                res -= 2 * roman[s[i-1]]
            res += roman[s[i]]
        return res
# @lc code=end
