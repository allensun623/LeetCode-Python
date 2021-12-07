'''
https://www.1point3acres.com/bbs/thread-825029-1-1.html
Youtube工作的黑人小哥哥，面试的时候话很少
Lumber cutting, given M * N size wood plank, price list for different sizes. What is the maximum profit?
Example: price list ---> 2*2 sells 3$, 2*3 sells 4$.
Cutting example: Given 6 * 2 size wood, can cut into 2X2 and 4X2, which can also be cut into 2X2 2X2 2X2, so the final profit (not max) is 9$.
这道题因为问max所以肯定是dp。dp其实就是穷举，labuladong说的。。‍‍‌‌‍‌‌‍‍‌‌‌‍‌‍‍‍‍‌。
我们这个木板，可以横着切也可以竖着切，穷举出来算max就好了。
比如这个木板，我们可以：
Horizontal cut : 6X1 6X1
Vertical cut:          5X2 1X2
                    4X2 2X2
                    3X2 3X2
用top down recursion加memo table。
面试官最后问了一下complexity。
'''


def lumber_cutting(m: int, n: int, cutting: dict) -> int:
    '''
    dp store store all max values
    double for loops to iterate through m * n
    for each size (r * c) -> for loop cutting options
    # edge check
    dp[r][c] = max(dp[r-i, c-j] + p for i, j in options if r >= i and c >= j)
    '''

    dp = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            dp[r][c] = max([dp[r-i][c-j] + p for (i, j),
                            p in cutting.items() if r >= i and c >= j] or [dp[r][c]])

    print(dp)
    return dp[-1][-1]


cutting = {
    (1, 2): 1,
    (1, 3): 2,
    (1, 4): 3,
    (1, 5): 4,
    (1, 6): 5,
    (2, 2): 2,
    (2, 3): 3,
    (2, 4): 4,
    (2, 5): 5,
    (2, 6): 6,
}

print(lumber_cutting(4, 6, cutting))
