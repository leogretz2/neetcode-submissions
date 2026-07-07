class TrieNode():
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.wordEnd = False
    
    def getChildren(self):
        return self.children

    def addChild(self, value: str, child: TrieNode):
        self.children[value] = child

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            # children publicly accessible?
            if c not in current.children:
                current.children[c] = TrieNode(c)
            current = current.children[c]

        current.wordEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            else:
                if current.children[c].wordEnd:
                    return True
                else:
                    current = current.children[c]
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            else:
                current = current.children[c]
        return True








