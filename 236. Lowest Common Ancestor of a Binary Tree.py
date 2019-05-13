"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.recurseTree(root, p, q)

    def recurseTree(self, root, p, q):
        if root is None:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        left = self.recurseTree(root.left, p, q)
        right = self.recurseTree(root.right, p, q)

        if left and right:
            return root
        else:
            if left:
                return left
            else:
                if right:
                    return right
                else:
                    return None


if __name__ == '__main__':
    root = TreeNode(3)

    # Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1

    node1 = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(0)
    node6 = TreeNode(8)
    node7 = TreeNode(7)
    node8 = TreeNode(4)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node4.left = node7
    node4.right = node8
    node2.left = node5
    node2.right = node6

    solution = Solution()
    print(solution.lowestCommonAncestor(root, node1, node8).val)
