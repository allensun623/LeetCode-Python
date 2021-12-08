
'''
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/
'''
# Trie vague search ['..a', 'b..a']


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
            cur = cur.nodes.setdefault(c, TrieNode())
        cur.is_leaf = True

    def search(self, word: str) -> bool:
        return self.search_node(word, self.root)

    def search_node(self, word: str, root: TrieNode) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                return any(self.search_node(word[i+1:], nxt) for nxt in root.nodes.values())
            if word[i] not in root.nodes:
                return False
            root = root.nodes[word[i]]

        return root.is_leaf
