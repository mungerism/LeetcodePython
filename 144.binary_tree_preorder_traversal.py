"""
144. Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

"""
二叉树
          0
      /       \
     1          2
   /   \       /  \
  3     4     5    6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            current_node = root
            stack = []
            result = []

            while current_node or stack:
                while current_node:
                    stack.append(current_node)
                    result.append(current_node.val)
                    current_node = current_node.left
                current_node = stack.pop()

                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node = None
        return  result

if __name__ == '__main__':
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    solution = Solution()
    solution.preorderTraversal(root)