class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]

        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.isEnd

            char = word[index]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):  # 從下一個找到的char開始往下找節點
                        return True
                return False

            if char in node.children:
                return dfs(
                    node.children[char], index + 1
                )  # 找到該字元的指向的Trie node, 繼續比對

            return False

        return dfs(self.root, 0)


# Time Complexity: O(26^n) n=word長度，當word所有字元都是wildcard時，每個節點最多可以有26個子節點

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
