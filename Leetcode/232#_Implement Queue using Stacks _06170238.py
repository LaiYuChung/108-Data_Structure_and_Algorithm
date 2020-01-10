
# coding: utf-8

# 2020 / 1 / 10 edit
# <br>From : leetcode 
# <br>Level : easy 
# <br>Qusetion : No.232 -- `Implement Queue using Stacks `

# Implement the following operations of a queue using stacks.
# 
# * push(x) -- Push element x to the back of queue.
# * pop() -- Removes the element from in front of queue.
# * peek() -- Get the front element.
# * empty() -- Return whether the queue is empty.

# In[ ]:


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        return self.que.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.que.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.que[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.que) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# Testcase:
# <br>["MyQueue","push","push","peek","pop","empty"]
# <br>[[],[1],[2],[],[],[]]

# Output:
# <br>[null,null,null,1,1,false]
