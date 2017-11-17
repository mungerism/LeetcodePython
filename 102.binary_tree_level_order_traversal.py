"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        else:
            queue = []
            result = []
            current_node = root
            result.append([current_node.val])
            queue.append(current_node)

            while queue:
                sub_queue = []
                sub = []
                while queue:
                    current_node = queue[0]
                    del queue[0]

                    if current_node.left or current_node.right:
                        if current_node.left:
                            sub.append(current_node.left.val)
                            sub_queue.append(current_node.left)
                        if current_node.right:
                            sub.append(current_node.right.val)
                            sub_queue.append(current_node.right)

                queue = sub_queue
                if queue:
                    result.append(sub)

            return result

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
    solution.levelOrder(root)