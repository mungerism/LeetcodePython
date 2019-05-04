"""
232. Implement Queue using Stacks

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.out_stack:
            return self.out_stack.pop()
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

            if self.out_stack:
                return self.out_stack.pop()
            else:
                return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.out_stack:
            return self.out_stack[len(self.in_stack) - 1]
        else:
            if self.in_stack:
                return self.in_stack[0]
            else:
                return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.in_stack or self.out_stack:
            return False
        else:
            return True


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    # print(obj.pop())
    print(obj.peek())
    print(obj.empty())


