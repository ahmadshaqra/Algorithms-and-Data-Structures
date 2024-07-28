"""
    Suffix Trie

    Function: Creates a suffix trie
    Space Complexity: O(n^2)

"""

from Trie import Trie

class SuffixTrie(Trie):

    def __init__(self, word: str) -> None:
        """
            Time Complexity: O(n^2)
        
        """

        # gets all suffixes of word
        suffixes = []
        for i in range(len(word)+1):
            suffixes.append(word[i:])
        
        # initialises suffix trie
        Trie.__init__(self, suffixes)

    def __contains__(self, substring: str) -> bool:
        """
            Time Complexity: O(m)
        
        """

        # traverses trie to end of the substring
        node = self.root
        for character in substring:

            # gets the index of the character
            index = ord(character) - 96

            # returns false if node not found, otherwise proceeds to next node
            if node[index] == None:
                return False
            node = node[index]
        
        # returns true if entire substring was traversed
        return True

if __name__ == '__main__':
    word = "referrer"
    trie = SuffixTrie(word)
    print(f"Trie: {trie}")
    print(f"'err' in Trie: {"err" in trie}")
    print(f"'fers' in Trie: {"fers" in trie}")
    