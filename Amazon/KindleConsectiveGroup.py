'''
input: s = '00110'
output: 3 ('0011', '01', '10')
1. The 0's and 1's are grouped consectively (e.g., 01, 10, 0011, 1100, 000111, etc)
2. The number of 0's in the substring is equal to the number of 1's in the substring.
'''

def group(s: str) -> int:
  # get max Os1s and max 1s0s
  nums = {
    '0': int(s[0] == '0'),
    '1': int(s[0] == '1'),
  }
  res = {
    '0': 0,
    '1': 0,
  }
  
  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      nums[s[i]] += 1
    else:
      nums[s[i]] = 1
    res[s[i]] = max(res[s[i]], min(nums.values()))

  return sum(res.values())

print(group('00111000'))
  
  
  