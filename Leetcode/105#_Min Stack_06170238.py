
# coding: utf-8

# 2020 / 1 / 8 edit
# <br>From : leetcode 
# <br>Level : easy 
# <br>Qusetion : No.105 -- `Min Stack`

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# 
# * push(x) -- Push element x onto stack.
# * pop() -- Removes the element on top of the stack.
# * top() -- Get the top element.
# * getMin() -- Retrieve the minimum element in the stack.

# In[ ]:


class MinStack:
    def __init__(self):
        self.list = []
        
    def push(self, x: int) -> None:            
        return self.list.append(x)

    def pop(self) -> None:
        return self.list.pop(-1)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Testcase:
# <br>["MinStack","push","push","push","getMin","pop","top","getMin"]
# <br>[[],[-2],[0],[-3],[],[],[],[]]

# Output:
# <br>[null,null,null,null,-3,null,0,-2]
