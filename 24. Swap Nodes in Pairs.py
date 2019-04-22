"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        curr_node = head
        pre_node = None
        next_node = None

        if head is not None and head.next is not None:
            head = head.next

        while curr_node is not None and curr_node.next is not None:
            next_node = curr_node.next
            tmp_node = next_node.next
            next_node.next = curr_node
            curr_node.next = tmp_node
            if pre_node is not None:
                pre_node.next = next_node

            pre_node = curr_node
            curr_node = curr_node.next

        return head

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = node1
    while (head is not None):
        print(head.val)
        head = head.next

    print()
    solution = Solution()
    head = solution.swapPairs(node1)

    while(head is not None):
        print(head.val)
        head = head.next
