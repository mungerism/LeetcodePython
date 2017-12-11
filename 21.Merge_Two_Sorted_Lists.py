"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = current = ListNode(0)

        while l1 or l2:

            if l1 and l2:

                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            else:
                if l1:
                    current.next = l1
                    l1 = None
                else:
                    current.next = l2
                    l2 = None

        return head.next

if __name__ == '__main__':
    node1_0 = ListNode(0)
    node1_1 = ListNode(1)
    node1_2 = ListNode(2)

    node2_0 = ListNode(0)
    node2_1 = ListNode(1)

    node1_0.next = node1_1
    node1_1.next = node1_2
    node2_0.next = node2_1

    solution = Solution()
    head = solution.mergeTwoLists(node1_0, node2_0)
    pass
