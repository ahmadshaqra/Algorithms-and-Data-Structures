"""
    Suffix Array

    Function: Creates a suffix array
    Space Complexity: O(n^2)

"""

class SuffixArray:

    def __init__(self, word: str) -> None:
        """
            Time Complexity: O(n*log(n))
        
        """

        # gets all suffixes of word and appends to array
        self.array = []
        for i in range(len(word)+1):
            self.array.append(word[i:] + '$')
        
        # sorts the array
        self.array.sort()

    def __contains__(self, substring: str) -> bool:
        """
            Time Complexity: O(m*log(n))

        """

        # uses a binary search algorithm to find substring in array
        lo = 0
        hi = len(self.array)
        while (lo <= hi):

            # sets mid pointer to middle of list
            mid = (lo + hi) // 2

            # checks if substring is at mid pointer
            if len(substring) <= len(self.array[mid]):
                is_substring = True
                for i in range(len(substring)):
                    if substring[i] != self.array[mid][i]:
                        is_substring = False
                if is_substring:
                    return True

            # checks where substring is relative to mid and changes pointers accordingly
            if substring > self.array[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        # returns false if substring is not found
        return False

    def __str__(self) -> str:
        """
            Time Complexity: O(n)

        """
        
        # returns a list of suffixes in alphabetical order
        return str([substring[:-1] for substring in self.array])
    
if __name__ == '__main__':
    word = "mississippi"
    array = SuffixArray(word)
    print(f"Suffix Array: {array}")
    print(f"'ipp' in Array: {"ipp" in array}")
    print(f"'ippim' in Array: {"ippim" in array}")
    