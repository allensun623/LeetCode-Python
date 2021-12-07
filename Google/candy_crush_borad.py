'''
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=825029&ctid=232507
Q2. Candy crush board, create starting board.
第二题没时间了，所以就讲了一下我的logic 和 time complexity。
这道题大致意思是刚开始的board不能有任何能消除的。消除条件是3个横着的或者竖着的。问我怎么initialize这个board。这个board必须是random，像这样
A B A C A
A B A B B
B A C A C
B B A A C
我说用一个三维matrix，前两维存board，第三维存横竖从左上角数现在有几个一样的A，B，C了。
聊了一下complexity。
'''

# m * n board, candy = ['A', 'B', 'C']

import random


def init_board(n: int, m: int, candy: list) -> list:
    # Init board
    # double for loop interate through rows, cols
    # each point (r, c), init options cur = {'A', 'B', 'C'}
    # r > 1, board[r-2][c] == board[r-1][c] -> remove board[r-1][c] in cur
    # c > 1, board[r][c-2] == board[r][c-1] -> remove board[r][c-1] in cur
    # board[r][c] = random from cur
    board = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            cur = set(candy)
            if r > 1 and board[r-2][c] == board[r-1][c]:
                cur.remove(board[r-1][c])
            if c > 1 and board[r][c-2] == board[r][c-1]:
                cur.remove(board[r][c-1])

            board[r][c] = random.choice(tuple(cur))

    return board


candy = ['A', 'B', 'C']
print(init_board(3, 3, candy))
