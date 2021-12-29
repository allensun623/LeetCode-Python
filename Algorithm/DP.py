
# * 1、第一种思路模板是一个一维的 dp 数组：

n = len(arr)
dp = [0] * n

for i in range(n):
    for j in range(i):
        dp[i] = 最值(dp[i], dp[j] + ...)

# * 2、第二种思路模板是一个二维的 dp 数组：
n = len(arr)
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] == arr[j]:
            dp[i][j] = dp[i][j] + ...
        else:
            dp[i][j] = 最值(...)

