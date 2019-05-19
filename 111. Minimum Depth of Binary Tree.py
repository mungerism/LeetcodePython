"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        depth = 1

        return self.recurse(root, depth)

    def recurse(self, root, depth):
        if root.left is None and root.right is None:
            return depth

        depth = depth + 1

        if root.left:
            left_depth = self.recurse(root.left, depth)

        if root.right:
            right_depth = self.recurse(root.right, depth)

        if root.left is None:
            left_depth = right_depth

        if root.right is None:
            right_depth = left_depth

        return min(left_depth, right_depth)


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
    print(solution.minDepth(root))
