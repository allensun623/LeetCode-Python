'''
https://www.1point3acres.com/bbs/thread-840849-1-1.html
Q2 给一串股票数字，在这串数字中找一个点index，0-index之间求个平均数，
剩下的index+1到末尾求个平均数，算出两个平均数之间的差值，
找出绝对值最小差值情况，index的数值是哪个(有重复，则返回最小的index)。
e.g,[1,3,2,3], 最小数值是2，[1,3]的平均数2, [2,3]平均数取整也为2，两个平均数差值为0，
所以从第二个月分开，平均数差值最小，结果返回2. （java中‍‍‌‍‌‌‌‌‍‍‌‍‌‌‌‍‌‌‌‌输入参数是List<Integer> stockPrice）
'''

# Time: O(N)
# Space: O(1)

def stack_price(stock: list) -> int:
  pos_sum = sum(stock)
  pre_sum = 0
  min_diff = float('inf')
  min_idx = 0
  n = len(stock)
  for i, x in enumerate(stock[:-1]):
    pos_sum -= x
    pre_sum += x
    cur_diff = abs(pos_sum // (n - i - 1) - pre_sum // (i + 1))
    if cur_diff < min_diff:
      min_diff = cur_diff
      min_idx = i
  
  return min_idx + 1

print(stack_price([1, 1, 2, 4, 2, 3]))