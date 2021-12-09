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
