# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
1. 找到旧的尾部并将其与链表头相连 old_tail.next = head，整个链表闭合成环，同时计算出链表的长度 n。
2. 找到新的尾部，第 (n - k % n - 1) 个节点 ，新的链表头是第 (n - k % n) 个节点。
3. 断开环 new_tail.next = None，并返回新的链表头 new_head
"""


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        current = head
        if current is None or current.next is None:
            return head

        length = 1

        while current.next:
            length += 1
            current = current.next

        current.next = head

        new_tail = self.findNewTail(head, length, k)
        new_head = new_tail.next
        new_tail.next = None
        return new_head

    def findNewTail(self, head, length, k):
        position = length - k % length - 1
        tail = head
        for i in range(position):
            tail = tail.next

        return tail
