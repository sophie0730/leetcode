class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:    
        node = self.root # create a pointer to point root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode() # create a new node
            node = node.children[index] # move the pointer to the new node
        node.isEnd = True #insert end, mark as the end of the word
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:     
                return False
            node = node.children[index] 

        return node.isEnd # determin if the pointer point the end of the word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.children[index]:     
                return False
            node = node.children[index]

        return True # if the prefix can be find in the node.children, return True

# time complexity: 
# insert: O(n), n = the length of the word
# search: O(n)
# prefix search: O(n)
            

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)