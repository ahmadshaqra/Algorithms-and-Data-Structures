"""
    Hash Table

    Function: Creates a hash table using chaining
    Space Complexity: O(n)

"""

from typing import TypeVar
T = TypeVar('T')

class HashTable:

    def __init__(self, max_size: int) -> None:
        """
            Time Complexity: O(n)
       
        """

        # initialises hash table
        self.table = [[] for _ in range(max_size)]
        self.size = 0
    
    def __setitem__(self, key: int, item: T) -> None:
        """
            Time Complexity (Average): O(1)
       
        """

        # gets hash value
        index = self.hash(key)

        # searches through chain to check for a duplicate key
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                raise ValueError("Inserting Duplicate Key")
        
        # adds item to the table
        self.table[index].append((key, item))
        self.size += 1

    def __delitem__(self, key: int) -> None:
        """
            Time Complexity (Average): O(1)
       
        """
        
        # gets hash value
        index = self.hash(key)

        # searches through chain to delete the item
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                del self.table[index][i]
                self.size -= 1
                return None
        
        # raises error because key was not found
        raise KeyError("Key Not Found")

    def __getitem__(self, key: int) -> T:
        """
            Time Complexity (Average): O(1)
       
        """

        # gets hash value
        index = self.hash(key)

        # searches through chain to return item
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                return self.table[index][i][1]
        
        # raises error because key was not found
        raise KeyError("Key Not Found")

    def __contains__(self, key: int) -> None:
        """
            Time Complexity (Average): O(1)
       
        """
        
        # attempts to get item with key
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def hash(self, key: int) -> int:
        """
            Time Complexity: O(1)
        
        """

        # returns hash value
        return (key % len(self.table))

    def __len__(self) -> int:
        """
            Time Complexity: O(1)

        """
        
        # returns size of table
        return self.size

    def __str__(self) -> str:
        """
            Time Complexity: O(n)
       
        """

        # returns string of hash table
        return str(self.table)

if __name__ == '__main__':
    table = HashTable(8)
    table[4] = "Seasons"
    table[1] = "World"
    table[5] = "Guys"
    table[10] = "Commandments"
    table[2] = "Partners"
    print(f"Hash Table:\n{table}\n")
    print(f"Item of Key 4: {table[4]}")
    print(f"Number of Items: {len(table)}")
    print(f"Table Contains 10: {10 in table}")
    print("Deleting Key 10\n")
    del table[10]
    print(f"Hash Table:\n{table}\n")
    print(f"Number of Items: {len(table)}")
    print(f"Table Contains 10: {10 in table}")
    print("Adding Key 5")
    try:
        table[5] = "Whoops"
    except ValueError:
        print("Value Error: Inserting Duplicate Key")
    