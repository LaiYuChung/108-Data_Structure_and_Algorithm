
# coding: utf-8

# Queue and Stack 實作
# 
# <br>功能:
# * Queueing : Queue排列(先進先出)
# * Stacking : Stack排列(後進先出)
# <br>   
# * outstack : Queue離開排列
# * dequeue  : Stack離開排列
# <br> 
# * show_now : 檢視目前排列情況

# In[1]:


class stack:
    def __init__(self):
        self.arr = []
    def stacking(self,num):
        self.arr.append(num)
        return "adding... {}".format(num)
    def outstack(self):
        self.arr.pop()
    def show_now(self):
        return self.arr
class queue:
    def __init__(self):
        self.arr = []
    def queueing(self,num):
        self.arr.append(num)
    def dequeue(self):
        self.arr.remove(self.arr[0])
    def show_now(self):
        return self.arr


# In[2]:


s = stack()
s.show_now()
print(s.stacking(1))
print(s.show_now())
print(s.stacking(2))
print(s.stacking(3))
print(s.stacking(4))
print(s.show_now())
s.outstack()
print(s.show_now())


# In[3]:


q = queue()
print(q.show_now())
q.queueing(2)
print(q.show_now())
q.queueing(3)
q.queueing(4)
q.queueing(5)
print(q.show_now())
q.dequeue()
print(q.show_now())

