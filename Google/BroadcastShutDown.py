# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=826251&ctid=232507
'''
Let's define a kind of message called "Broadcast & Shut Down." When a router receives this message, it broadcasts the
same message to all other routers within its wireless range. Then, that router shuts down, and can no longer send or
receive messages.

For example, Router A is at (0, 0); Router B is at (0, 8); Router C is at (0, 17); Router D is at (11, 0). If the
wireless range is 10, when Router A send a message, it could first reach B; the message from Router B will further reach
Router C. But Router D will never receive this message.
A 0 0
B 0 8
C 0 17
D 11 0
问：Given a list of routers' locations (their names and the corresponding 2D coordinates), tell me whether a message from
Router A can reach Router B. Write a method / function with appropriate input and output arguments.
'''


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return None
        less, more = (rx, ry) if self.size[rx] < self.size[ry] else (ry, rx)
        self.size[more] += less
        self.parent[less] = self.parent[more]
        return None

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def hypotenuse(p1, p2) -> float:
    a = abs(p1[0] - p2[0]) ** 2
    b = abs(p1[1] - p2[1]) ** 2
    return (a + b) ** (1 / 2)


def broadcast(x, y) -> bool:
    arr = [(0, 0), (0, 8), (0, 17), (11, 0)]
    n = len(arr)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if hypotenuse(arr[i], arr[j]) <= 10:
                uf.union(i, j)

    return uf.connected(x, y)


print(broadcast(0, 3))
