class Different:
    def __init__(self, nums: list) -> None:
        self.df = self.difference(nums)


def difference(self, nums: list):
    df = nums[0]
    for x in nums[1:]:
        df.append(x - df[-1])
    return df


def increase(self, i: int, j: int, val: int):
    self.df[i] += val
    if j + i < len(self.df):
        self.df[j+1] -= val


def result(self):
    res = self.df[:]
    for i in range(1, len(res)):
        res[i] += res[i-1]
    return res
