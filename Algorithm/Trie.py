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
