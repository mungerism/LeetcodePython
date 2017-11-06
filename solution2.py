"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_node1 = l1
        head_node2 = l2
        add = 0
        is_head = True

        while True:
            if head_node1 == None and head_node2 == None and add == 0:
                break
            else:
                if head_node1 == None:
                    head_node1 = ListNode(0)

                if head_node2 == None:
                    head_node2 = ListNode(0)

            total = head_node1.val + head_node2.val + add

            new_node = ListNode(total % 10)

            if is_head:
                head_node = new_node
            else:
                current_node.next = new_node

            current_node = new_node
            add = 1 if total >= 10 else 0
            is_head = False
            head_node1 = head_node1.next
            head_node2 = head_node2.next

        return head_node

if __name__ == '__main__':

    head_node1 = ListNode(0)
    head_node2 = ListNode(1)
    node11 = ListNode(8)
    head_node1.next = node11

    solution = Solution()
    head_node = solution.addTwoNumbers(head_node1, head_node2)