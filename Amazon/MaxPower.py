'''
https://www.1point3acres.com/bbs/thread-841736-1-1.html
bootingPower = [3, 6, 1, 3, 4]
processingPower = [2, 1, 3, 4, 5]
powerMax = 25

e.g.
max bootup = max([3, 6, 4]) = 6
k = len([3, 6, 4]) = 3
usage = 6 + 3 * 6


'''
from collections import deque

def maxPowerConsumption(bootingPower: list, processingPower: list, powerMax: int) -> int:
  pq = deque()
  res = total = i = 0
  for j in range(len(bootingPower)):
    total += processingPower[j]
    # update max value in pq
    while pq and bootingPower[pq[-1]] < bootingPower[j]:
      pq.pop()
    pq.append(j)
    # left pointer moves while power > powerMax
    if bootingPower[pq[0]] + (total) * (j - i + 1) > powerMax:
      total -= processingPower[i]
      i += 1
      while pq and pq[0] < i:
        pq.popleft()
    
    res = max(res, j - i + 1)
    
  return res
    

print(maxPowerConsumption([3, 6, 1, 3, 4, 2, 1, 1, 1, 1], [2, 1, 3, 4, 5, 1, 1, 1, 1, 1], 25))
