"""
107. Binary Tree Level Order Traversal II
Easy

714

133

Favorite

Share
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):

        if root is None:
            return []

        result = collections.deque([])
        roots = [root]
        values = [root.val]

        while roots:
            if values:
                result.appendleft(values)
            roots, values = self.get_next_level_children(roots)

        return list(result)

    def get_next_level_children(self, roots):
        children = []
        values = []
        for root in roots:
            if root.left is not None:
                children.append(root.left)
                values.append(root.left.val)

            if root.right is not None:
                children.append(root.right)
                values.append(root.right.val)

        return children, values


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

    print(solution.levelOrderBottom(root))
