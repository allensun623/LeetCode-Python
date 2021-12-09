'''
https://zhuanlan.zhihu.com/p/335793141
https://blog.csdn.net/haolexiao/article/details/69218215
https://blog.csdn.net/ANNILingMo/article/details/80879910
https://blog.csdn.net/weixin_43204128/article/details/90633128?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link
https://www.pythonf.cn/read/77082
https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/

https://stackoverflow.com/questions/13032116/trie-complexity-and-searching
Time: O(N)
Space: O(N*|S|)
The complexity of creating a trie is O(W*L), 
where W is the number of words, and L is an average length of the word: 
you need to perform L lookups on the average for each of the W words in the set.


'''


class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            # if c not in cur.nodes:
            #     cur.nodes[c] = TrieNode()
            # cur = cur.nodes[c]
            cur = cur.nodes.setdefault(c, TrieNode())
        cur.is_leaf = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        return cur.is_leaf

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        return True

    def find_prefix(self, word: str) -> bool:
        '''
        if lexicon contains a prefix of the word, return the prefix else
        else return the word
        '''
        cur = self.root
        for i, c in enumerate(word):
            if cur.is_leaf:
                return word[:i]

            if c not in cur.nodes:
                return word
            cur = cur.nodes[c]

        return word

    def longest_common_prefix(self, word: str) -> str:
        cur = self.root
        prefix = ''
        for c in word:
            if c not in cur.nodes or cur.is_leaf or len(cur.nodes) != 1:
                break
            prefix += c
            cur = cur.nodes[c]
        return prefix
