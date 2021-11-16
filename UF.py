class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            less, more = (
                rx, ry) if self.size[rx] < self.size[ry] else (ry, rx)
            self.parent[less] = more
            self.size[more] += self.size[less]
            self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    # def count(self):
    #     return sum(i == x for i, x in enumerate(self.parent))
    #     return len{self.find(x) for x in parent}
