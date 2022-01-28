import pysnooper
import string
import heapq


class KthLargest:

    # Second
    def __init__(self, k: int, nums: list):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# @pysnooper.snoop()
def test():
    # print(list(string.ascii_lowercase))
    stack = [2, 3, 4]
    heapq.heapify(stack)
    print(stack)
    # [3, 2, 4]
    heapq.heappush(stack, 6)
    print(stack)
    # [3, 2, 4]
    heapq.heappushpop(stack, 5)
    print(stack)
    heapq.heappop(stack)
    print(stack)


class UF:
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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


def union_find(n, edges):
    uf = UF(n)
    for x, y in edges:
        if uf.connected(x, y):
            return False
        uf.union(x, y)

    return uf.count == 1


def main():
    # test()

    print(union_find(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))


if __name__ == '__main__':
    main()


