'''
E.G.
input: 'ababaa'
output: 11
The suffixes are ['ababaa', 'babaa', 'abaa', 'baa', 'aa', 'a'].
The common prefix lengths of each of there suffixes
[6, 0, 3, 0, 1, 1], sum = 11
'''
# Time: O(N^2)
# Space: O(1)
def sum_of_common_suffix(s: str) -> int:
  res = 0
  n = len(s)
  for i in range(n):
    j = 0
    while i + j < n and s[i + j] == s[j]:
      j += 1
    res += j
  
  return res
  


print(sum_of_common_suffix('ababaa'))