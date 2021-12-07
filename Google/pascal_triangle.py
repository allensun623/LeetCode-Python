'''
https://www.1point3acres.com/bbs/thread-826251-1-1.html
给一个matrix，再给一个x和y，返回他的值。
我一开始以为matrix是给定的，就说了想法，开始写。其实理解题目是错的，大哥也不管。
我写完后，大哥说，matrix是这样的：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
'''


def get_pascal_val(x, y):
    a, b = 1, y - x
    for _ in range(x):
        a, b = a + b,


# First with DFS
def get_pascal_value(x, y):
    if x > y:
        return -1

    def dfs(x, y):
        if x == 0 or x == y:
            return 1
        if x == 1 or x + 1 == y:
            return y
        return dfs(x-1, y-1) + dfs(x, y-1)

    return dfs(x, y)


def main():
    print(get_pascal_value(3, 6))


if __name__ == '__main__':
    main()
