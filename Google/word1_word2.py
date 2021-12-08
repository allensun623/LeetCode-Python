'''
全大写word1，add a single character and shuffle得到word2，
给你word1 word2问你word2能不能由word1得到。
example：word1: 'ACT' -> add 'K' -> 'ACTK' -> shuffle -> word2 = 'TACK' 
example 2: word1 = 'ACT', word2 = 'TASK' -> False.  
character可以duplicate
follow up：给两个list of words，问你出书list2里所有可以由list1里的word变换而来的words，
example：
    list1 = ['ACT', 'THE', 'ASK'], list2 = ['TACK', 'BAT', 'TASK', 'FACT'], 
output = ['TACK', 'TASK', 'FACT']. 
lz给出double loop的brute force解法o(mn) m n是两个list的长度，
继续follow up，问能不能optimize time complexity，
把里面那个loop变成constant，变成o(m) or o(n)
'''

'''
    word1 + c is the permutation of word2
    count frequency of word2, and word1
    diff = 0 
    cnt1 = Counter(word1)
    cnt2 = Counter(word2)
    for loop to iterate character, frequency in cn2:
        diff = cnt2[character] - cnt1[character]
    return diff == 1
'''


def count(word: str) -> dict:
    cnt = {}
    for c in word:
        cnt[c] = cnt.get(c, 0) + 1
    return cnt

# Dict
def word_shuffle_math(word1: str, word2: str) -> bool:
    if len(word2) - len(word1) != 1:
        return False
    cnt1 = count(word1)
    cnt2 = count(word2)
    diff = 0
    for k, v2 in cnt2.items():
        v1 = cnt1.get(k, 0)
        if v1 > v2:
            return False
        diff += v2 - v1

    return diff == 1

# BitMap
def count(word: str) -> list:
    cnt = [0] * 26
    for c in word:
      cnt[ord(c) - ord('A')] += 1
    return cnt

def word_shuffle_math(word1: str, word2: str) -> bool:
    if len(word2) - len(word1) != 1:
        return False
    cnt1 = count(word1)
    cnt2 = count(word2)
    diff = 0
    for i, v2 in enumerate(cnt2):
        v1 = cnt1[i]
        if v1 > v2:
            return False
        diff += v2 - v1

    return diff == 1



print(word_shuffle_math('ASDFD', 'ASDFSD'))


def words(list1: list, list2: list) -> list:
    res = []
    for word2 in list2:
        if any(word_shuffle_math(word1, word2) for word1 in list1):
            res.append(word2)

    return res
    # return [word2 for word2 in list2 if any(word_shuffle_math(word1, word2) for word1 in list1)]

def words(list1: list, list2: list) -> list:
    bag = {
      
    }
list1 = ['ACT', 'THE', 'ASK']
list2 = ['TACK', 'BAT', 'TASK', 'FACT']
# output = ['TACK', 'TASK', 'FACT'].
print(words(list1, list2))
