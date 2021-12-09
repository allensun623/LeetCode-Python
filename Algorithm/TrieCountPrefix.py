'''
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=815871&ctid=232507
狗家VO，工作经验2年，面L4，今天刚面的，一共五轮，趁着还记得，回馈地里，就不设分数限制了，求加米～
1. 国人小姐姐，给一个Alphabetically sorted String array和一个prefix，
求这个array里面一共有多少个以这个prefix开头的String。
做两次binary search找到第一个和最后一个符合要求的index然后相减。
Follow up，如果有非常多次Query with prefix操作该怎么办。那么是时候祭出Trie了。
白板手动test code，以及问了时间复杂度。
'''


class TrieNode:
    def __init__(self) -> None:
        self.nodes = {}
        self.is_leaf = False
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur.count += 1
            cur = cur.nodes.setdefault(c, TrieNode())
        cur.is_leaf = True

    def count_prefix(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            cur = cur.nodes[c]
            print(c, cur.nodes.keys(), cur.count)
        return cur.count


def count_prefix(prefix: str, word: list) -> int:
    trie = Trie()
    for word in words:
        trie.insert(word)

    return trie.count_prefix(prefix)


words = ['a', 'asdf', 'asdfd', 'asfsdf', 'qqq', 'aad', 'asz']
prefix = 'a'
print(count_prefix(prefix, words))
