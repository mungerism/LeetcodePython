"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
from queue import PriorityQueue


class KthLargest:

    def __init__(self, k: int, nums):
        self.q = PriorityQueue()
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.q.qsize() < self.k:
            self.q.put(val)
            return val
        else:
            min_value = self.q.queue[0]
            if val > min_value:
                self.q.get()  # 取出并移除第一个元素（最小）
                self.q.put(val)
                return self.q.queue[0]
            else:
                return min_value


if __name__ == '__main__':
    # Your KthLargest object will be instantiated and called as such:
    obj = KthLargest(1, [])
    print(obj.add(10))
    # a = PriorityQueue()
    #
    # a.put(10)
    # a.put(4)
    # a.put(3)
    #
    # print(a.queue[0])
