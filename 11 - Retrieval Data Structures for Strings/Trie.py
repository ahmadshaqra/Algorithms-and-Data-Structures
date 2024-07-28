"""
    Trie

    Function: Creates a trie
    Space Complexity: O(n*m)

"""

class Trie:

    def __init__(self, words: list[str]) -> None:
        """
            Time Complexity: O(n*m)
        
        """

        # initialises root node
        self.root = [None for _ in range(27)]

        # inserts words into trie
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        """
            Time Complexity: O(m)
        
        """

        # traverses trie to end of the word
        node = self.root
        for character in word:

            # gets the index of the character
            index = ord(character) - 96

            # adds node if required then proceeds to next node
            if node[index] == None:
                node[index] = [None for _ in range(27)]
            node = node[index]
        
        # adds tag at the end of the word
        node[0] = ('$', word)

    def __contains__(self, word: str) -> bool:
        """
            Time Complexity: O(m)
        
        """

        # traverses trie to end of the word
        node = self.root
        for character in word:

            # gets the index of the character
            index = ord(character) - 96

            # returns false if node not found, otherwise proceeds to next node
            if node[index] == None:
                return False
            node = node[index]
        
        # checks tag at the end of the word
        if node[0] == ('$', word):
            return True
        return False

    def prefix_search(self, prefix: str) -> list[str] | None:
        """
            Time Complexity: O(m+n)
        
        """

        # traverses trie to last prefix character
        node = self.root
        for character in prefix:

            # gets the index of the character
            index = ord(character) - 96

            # returns none if node not found, otherwise proceeds to next node
            if node[index] == None:
                return None
            node = node[index]
        
        # returns list of words in subtree rooted at node
        return self.get_words(node)
    
    def get_words(self, node: list, words: list[str] = None) -> list[str]:
        """
            Time Complexity: O(n)
        
        """
        
        # initialises words list
        if words == None:
            words = []

        # checks if node is none
        if node == None:
            return words
        else:

            # checks if node is at the end of a word
            if node[0] != None:
                words.append(node[0][1])
            
            # traverses every child node in alphabetical order
            for i in range(1, 26):
                words = self.get_words(node[i], words)

        # returns list of words in subtree
        return words

    def __str__(self) -> str:
        """
            Time Complexity: O(m+n)
        
        """
        
        # returns list of words in trie in alphabetical order
        return str(self.prefix_search(""))
        
if __name__ == '__main__':
    words = ["baby", "bad", "bank", "box", "dog", "dogs", "banks"]
    trie = Trie(words)
    print(f"Trie: {trie}")
    print(f"'bank' in Trie: {"bank" in trie}")
    print(f"'coffee' in Trie: {"coffee" in trie}")
    print(f"Prefix of 'b': {trie.prefix_search("b")}")
    