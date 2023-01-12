'''

             ROOT
             |   \
             a    b
             |      \
             p         a
             |            \     
             p.end = True   t.end = True



ROOT   children = {a : ab1a, b : ab1b}
a      children = {p : 1234}
p      children = {p : 1235}
p      children = {}

b      children = {a : 1236}
a      children = {t : 1237}
t      children = {}


'''


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False 


class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        
        current_node = self.root
        
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()

            #Advance to next node
            current_node = current_node.children[letter]
        
        current_node.is_end_of_word = True


    def search(self, word: str) -> bool:

        current_node = self.root

        for letter in word:
            if not letter in current_node.children:
                return False

             #Advance to next node   
            current_node = current_node.children[letter]
            
        return current_node.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:

        current_node = self.root

        for letter in prefix:
            if letter not in current_node.children:
                return False
            
            #Advance to next node
            current_node = current_node.children[letter]
            
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)