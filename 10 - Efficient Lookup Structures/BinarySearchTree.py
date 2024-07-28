"""
    Binary Search Tree

    Function: Creates a binary search tree
    Space Complexity: O(n)

"""

from typing import TypeVar
K = TypeVar('K')
I = TypeVar('I')

class TreeNode:

    def __init__(self, key: K, item: I) -> None:
        """
            Time Complexity: O(1)

        """
        
        # initialises tree node
        self.key = key
        self.item = item
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self) -> None:
        """
            Time Complexity: O(1)

        """

        # initialises binary search tree
        self.root = None
        self.size = 0

    def __setitem__(self, key: K, item: I) -> None:
        """
            Time Complexity: O(n)

        """

        # inserts item into binary search tree
        self.root = self.insert(self.root, key, item)

    def insert(self, node: TreeNode, key: K, item: I) -> TreeNode:
        """
            Time Complexity: O(n)

        """

        # reaches correct position and inserts node
        if node == None:
            node = TreeNode(key, item)
            self.size += 1
        
        # found a node with the same key and raises an error
        elif node.key == key:
            raise ValueError("Inserting Duplicate Key")
        
        # key is greater than node so inserts to the right of the node
        elif node.key < key:
            node.right = self.insert(node.right, key, item)

        # key is less than node so inserts to the left of the node
        elif node.key > key:
            node.left = self.insert(node.left, key, item)
        
        # returns node
        return node

    def __delitem__(self, key: K) -> None:
        """
            Time Complexity: O(n)

        """

        # deletes item from binary search tree
        self.root = self.delete(self.root, key)
    
    def delete(self, node: TreeNode, key: K) -> TreeNode:
        """
            Time Complexity: O(n)
        
        """

        # reaches bottom of tree without finding key and raises an error
        if node == None:
            raise KeyError("Key Not Found")
        
        # finds node and deletes it
        elif node.key == key:

            # case 1: node is leaf node
            if node.left == None and node.right == None:
                self.size -= 1
                return None

            # case 2: node has no left child
            elif node.left == None:
                self.size -= 1
                return node.right
            
            # case 3: node has no right child
            elif node.right == None:
                self.size -= 1
                return node.left
            
            # case 4: node is root of subtree
            else:
                successor = self.get_successor(node)
                node.key  = successor.key
                node.item = successor.item
                node.right = self.delete(node.right, successor.key)
        
        # key is greater than node so continues search in the right subtree
        elif node.key < key:
            node.right = self.delete(node.right, key)

        # key is less than node so continues search in the left subtree
        elif node.key > key:
            node.left = self.delete(node.left, key)
        
        # returns current node
        return node

    def __getitem__(self, key: K) -> I:
        """
            Time Complexity: O(n)

        """

        # searches for item in binary search tree
        return self.get_node(self.root, key).item
        
    def get_node(self, node: TreeNode, key: K) -> TreeNode:
        """
            Time Complexity: O(n)

        """

        # reaches bottom of tree without finding key and raises an error
        if node == None:
            raise KeyError("Key Not Found")
        
        # finds and returns node
        elif node.key == key:
            return node

        # key is greater than node so continues search in the right subtree
        elif node.key < key:
            return self.get_node(node.right, key)
        
        # key is less than node so continues search in the left subtree
        elif node.key > key:
            return self.get_node(node.left, key)

    def __contains__(self, key: K) -> bool:
        """
            Time Complexity: O(n)
       
        """
        
        # attempts to get node from key
        try:
            _ = self[key]
        
        # error is raised and node is not in binary search tree
        except KeyError:
            return False

        # no error is raised and node is in binary search tree
        else:
            return True
    
    def get_successor(self, node: TreeNode) -> TreeNode:
        """
            Time Complexity: O(n)    
    
        """

        # sets node to the tree node on the right of the source
        node = node.right

        # node is none and source has no right child hence no successor
        if node == None:
            return None
        
        # finds and returns minimal node in right subtree
        else:
            next = node.left
            is_minimal = False
            while not is_minimal:
                if next == None:
                    is_minimal = True
                else:
                    node = next
                    next = node.left
            return node
    
    def __len__(self) -> int:
        """
            Time Complexity: O(1)

        """
        
        # returns size of tree
        return self.size
    
    def __str__(self) -> str:
        """
            Time Complexity: O(n)
        
        """

        # returns a string of a visual binary search tree
        output = self.draw(self.root)
        return output[:-1]

    def draw(self, node: TreeNode, prefix: str = "", final: str = "", output: str = None) -> str:
        """
            Time Complexity: O(n)

        """

        # draws a visual binary search tree
        if output == None:
            output = ""
        if node != None:
            real_prefix = prefix[:-2] + final
            output += f"{real_prefix}{node.key}\n"
            if node.left != None or node.right != None:
                output = self.draw(node.right, prefix + "\u2551 ", "\u255f\u2500", output)
                output = self.draw(node.left, prefix + "  ", "\u2559\u2500", output)
        else:
            real_prefix = prefix[:-2] + final
            output += f"{real_prefix}\n"
        return output

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree[10] = "Ten"
    tree[5] = "Five"
    tree[15] = "Fifteen"
    tree[3] = "Three"
    tree[7] = "Seven"
    tree[13] = "Thirteen"
    tree[17] = "Seventeen"
    tree[16] = "Sixteen"
    print(f"Binary Search Tree:\n{tree}\n")
    print(f"Item of Node 7: {tree[7]}")
    print(f"Number of Nodes: {len(tree)}")
    print(f"Tree Contains 15: {15 in tree}")
    print("Deleting Node 15\n")
    del tree[15]
    print(f"Binary Search Tree:\n{tree}\n")
    print(f"Number of Nodes: {len(tree)}")
    print(f"Tree Contains 15: {15 in tree}")
    