# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        len_a = self.get_count(headA)
        len_b = self.get_count(headB)
        
        diff_len = len_a - len_b

        if diff_len >= 0:
            for i in range(abs(diff_len)):
                headA = headA.next
        else:
            for i in range(abs(diff_len)):
                headB = headB.next

        while headA is not headB:
            
            if headA is None or headB is None:
                return None

            headA = headA.next
            headB = headB.next
        
        return headA


    def get_count(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

if __name__ == "__main__":
    node_a_1 = ListNode(2)
    node_a_2 = ListNode(4)
    node_a_3 = ListNode(6)
    node_a_4 = ListNode(8)
    node_a_5 = ListNode(10)
    node_a_6 = ListNode(11)
    node_a_7 = ListNode(12)
    node_a_8 = ListNode(13)
    node_a_9 = ListNode(14)
    node_a_10 = ListNode(15)
    node_a_11 = ListNode(16)
    node_a_12 = ListNode(17)
    node_a_13 = ListNode(18)
    node_a_14 = ListNode(19)
    node_a_15 = ListNode(20)
    node_a_16 = ListNode(21)
    node_a_17 = ListNode(22)
    node_a_18 = ListNode(23)
    node_a_19 = ListNode(24)

    node_a_1.next = node_a_2
    node_a_2.next = node_a_3
    node_a_3.next = node_a_4
    node_a_4.next = node_a_5
    node_a_5.next = node_a_6
    node_a_6.next = node_a_7
    node_a_7.next = node_a_8
    node_a_8.next = node_a_9
    node_a_9.next = node_a_10
    node_a_10.next = node_a_11
    node_a_11.next = node_a_12
    node_a_12.next = node_a_13
    node_a_13.next = node_a_14
    node_a_14.next = node_a_15
    node_a_15.next = node_a_16
    node_a_16.next = node_a_17
    node_a_17.next = node_a_18
    node_a_18.next = node_a_19


    solution = Solution()
    print(solution.getIntersectionNode(node_a_6, node_a_1).val)