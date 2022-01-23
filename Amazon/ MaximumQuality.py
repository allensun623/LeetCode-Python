'''
Amazon | OA | Maximum Quality
https://leetcode.com/discuss/interview-question/1641829/Amazon-or-OA-or-Maximum-Quality
'''



def maximun_quality(packets: list, channels: int) -> int:
  res = 0
  packets.sort()
  if channels > len(packets):
    return -1
  res += sum(packets[-channels+1:])
  m = (len(packets) - channels) // 2
  res += round((packets[m] + packets[-channels-m]) / 2)
  
  return res

test1 = ([5, 4, 2, 1, 7, 6, 3], 2)
print(maximun_quality(*test1))