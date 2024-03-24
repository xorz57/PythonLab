class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, string):
        current = self._root
        if current is None:
            return
        for character in string:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.leaf = True

    def contains(self, string):
        current = self._root
        if current is None:
            return False
        for character in string:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.leaf
