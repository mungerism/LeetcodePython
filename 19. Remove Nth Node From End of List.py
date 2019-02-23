"""
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        to_be_removed = head
        to_be_end = head
        before = None

        for i in range(0, n):
            to_be_end = to_be_end.next

        while to_be_end != None:
            to_be_end = to_be_end.next
            before = to_be_removed
            to_be_removed = to_be_removed.next

        if before == None:
            before = to_be_removed.next
            head = before
        else:
            before.next = to_be_removed.next

        return head


if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    head = solution.removeNthFromEnd(node1, 5)

    while head != None:
        print(head.val)
        head = head.next


