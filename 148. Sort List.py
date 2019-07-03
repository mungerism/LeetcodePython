# Definition for singly-linked list.

"""
148. Sort List

考点：
1. merge sort
2. fast/slow pointer split

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def sortList(self, head):
        return self.merge_sort(head)

    def front_back_split(self, source):

        front = None
        back = None

        if source is None or source.next is None:  # length < 2 cases
            front = source
            return front, back

        slow = source
        fast = source.next

        # Advance 'fast' two nodes, and advance 'slow' one node
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next

        # 'slow' is before the midpoint in the list, so split it in two at that point
        front = source
        back = slow.next
        slow.next = None
        return front, back

    def merge_sort(self, source):

        head = source

        if head is None or head.next is None:
            return head

        a, b = self.front_back_split(head)  # Split head into 'a' and 'b' sublists

        a = self.merge_sort(a)  # Recursively sort the sublists
        b = self.merge_sort(b)

        return self.sorted_merge(a, b)

    def sorted_merge(self, a, b):
        if a is None:
            return b
        else:
            if b is None:
                return a

        # Pick either a or b, and recur
        if a.val <= b.val:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node5.next = node4
    node4.next = node3
    node3.next = node2
    node2.next = node1

    solution = Solution()
    res = solution.merge_sort(node5)

    while res:
        print(res.val)
        res = res.next
