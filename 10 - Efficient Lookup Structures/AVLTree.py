"""
    AVL Tree

    Function: Creates an AVL tree resulting in O(log(n)) insertion, deletion, and searching
    Space Complexity: O(n)

"""

from BinarySearchTree import BinarySearchTree, TreeNode
from typing import TypeVar
K = TypeVar('K')
I = TypeVar('I')

class AVLTreeNode(TreeNode):

    def __init__(self, key: K, item: I) -> None:
        """
            Time Complexity: O(1)

        """
        
        # initialises tree node
        super(AVLTreeNode, self).__init__(key, item)
        self.height = 0

class AVLTree(BinarySearchTree):

    def insert(self, node: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            Time Complexity: O(log(n))

        """

        # reaches correct position and inserts node
        if node == None:
            node = AVLTreeNode(key, item)
            self.size += 1
            return node
        
        # found a node with the same key and raises an error
        elif node.key == key:
            raise ValueError("Inserting Duplicate Key")
        
        # key is greater than node so inserts to the right of the node
        elif node.key < key:
            node.right = self.insert(node.right, key, item)

        # key is less than node so inserts to the left of the node
        elif node.key > key:
            node.left = self.insert(node.left, key, item)
        
        # updates height
        self.update_height(node)

        # rebalances and returns node
        return self.rebalance(node)
    
    def delete(self, node: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            Time Complexity: O(log(n))
        
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
        
        # updates height
        self.update_height(node)

        # rebalances and returns node
        return self.rebalance(node)
    
    def get_height(self, node: AVLTreeNode) -> int:
        """
            Time Complexity: O(1)

        """

        # returns height of node
        if node != None:
            return node.height
        else:
            return -1
    
    def update_height(self, node: AVLTreeNode) -> None:
        """
            Time Complexity: O(1)
        
        """

        # updates height of node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance_factor(self, node: AVLTreeNode) -> int:
        """
            Time Complexity: O(1)
            
        """
        
        # returns balance factor of node
        if node == None:
            return 0
        else:
            return self.get_height(node.left) - self.get_height(node.right)
    
    def rebalance(self, root: AVLTreeNode) -> AVLTreeNode:
        """
            Time Complexity: O(1)

        """

        # checks if balance factor of root node is too high
        if self.get_balance_factor(root) >= 2:

            # case 1: left-right imbalance
            if self.get_balance_factor(root.left) < 0:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            
            # case 2: left-left imbalance
            else:
                return self.rotate_right(root)

        # checks if balance factor of root node is too low
        elif self.get_balance_factor(root) <= -2:

            # case 3: right-left imbalance
            if self.get_balance_factor(root.right) > 0:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

            # case 4: right-right imbalance
            else:
                return self.rotate_left(root)
        
        # case 5: no imbalance
        return root

    def rotate_right(self, root: AVLTreeNode) -> AVLTreeNode:
        """
            Time Complexity: O(1)

        """

        # labels nodes to be manipulated
        pivot = root.left
        center = pivot.right

        # rotates subtree
        pivot.right = root
        root.left = center

        # updates heights of nodes
        self.update_height(root)
        self.update_height(pivot)

        # checks if root node is tree root
        if root == self.root:
            self.root = pivot

        # returns new root node
        return pivot

    def rotate_left(self, root: AVLTreeNode) -> AVLTreeNode:
        """
            Time Complexity: O(1)

        """
        
        # labels nodes to be manipulated
        pivot = root.right
        center = pivot.left

        # rotates subtree
        pivot.left = root
        root.right = center

        # updates heights of nodes
        self.update_height(root)
        self.update_height(pivot)

        # checks if root node is tree root
        if root == self.root:
            self.root = pivot

        # returns new root node
        return pivot

if __name__ == '__main__':
    tree = AVLTree()
    for i in range(16):
        tree[i] = "🤖" * i
    print(f"AVL Tree:\n{tree}\n")
    print(f"Item of Node 5: {tree[5]}")
    print(f"Number of Nodes: {len(tree)}")
    print(f"Tree Contains 15: {15 in tree}")
    print("Deleting All Nodes Greater Than 7\n")
    for i in range(8, 16):
        del tree[i]
    print(f"AVL Tree:\n{tree}\n")
    print(f"Number of Nodes: {len(tree)}")
    print(f"Tree Contains 15: {15 in tree}")
    