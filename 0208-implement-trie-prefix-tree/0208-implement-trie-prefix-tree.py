class TrieNode:
    def __init__(self):
        self.children = {}            # hashmap to store characters of any word
        self.endOfWord = False        # this method checks whether word is ended

class Trie:

    def __init__(self):
        """
        This class constructor initializes an empty root node
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        To store/insert a word into a Trie
        """
        # create a current TrieNode equals to root.
        curr = self.root

        for char in word:
            # check is char is already a children of curr
            if char not in curr.children:
                # if not children, add a new TrieNode as its children
                curr.children[char] = TrieNode()
            # if already a child node
            curr = curr.children[char]

        # at the end of word assign last node as endOfWord
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        """
        To search for a word in a Trie
        """
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        # if all char of word are present endOfWord should be True else False
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        To check whether a word starts with a prefix
        """
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        # we need not to check for endOfWord status.
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)