"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # self.traverse(head)

        last_node = head
        first_node = head
        new_head = None
        pre_node = None

        i = 1
        while last_node:
            if i == k:
                if new_head is None:
                    new_head = last_node
                next_node = self.reverse(first_node, k)

                if pre_node:
                    pre_node.next = next_node

                # self.traverse(new_head)

                pre_node = first_node
                last_node = first_node.next
                first_node = first_node.next
                i = 0
            else:
                last_node = last_node.next

            i += 1

        if new_head is None:
            new_head = head
        return new_head

    def reverse(self, head, k):
        current_node = head
        pre_node = None

        i = 0
        while i < k:
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node
            i += 1

        head.next = current_node
        return pre_node

    # def traverse(self, head):
    #     print("----")
    #     while head:
    #         print(head.val)
    #         head = head.next
    #     print("----")

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    head = solution.reverseKGroup(node6, 2)
    solution.traverse(head)



