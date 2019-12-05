
# coding: utf-8

# In[ ]:


#Hash Table function
#2019/12/5
#function:add, remove, contains


# In[ ]:


#參考資料:https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/
#https://www.hackerearth.com/zh/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/


# In[1]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        h = MD5.new(key.encode("UTF-8"))
        h2 = h.hexdigest()
        num = int(h.hexdigest(),16) % self.capacity
        self.data = self.data[:num] + [h2] + self.data[num:]

    def remove(self, key):
        h = MD5.new(key.encode("UTF-8"))
        h2 = h.hexdigest()
        num = int(h.hexdigest(),16) % self.capacity
        if self.data[num:].count(h2) == 0:
            pass
        else:
            self.data.remove(h2)
            if self.data.count(h2)!=0:
                return self.remove(key)
            
    def contains(self, key):
        h = MD5.new(key.encode("UTF-8"))
        h2 = h.hexdigest()
        num = int(h.hexdigest(),16) % self.capacity
        b = self.data[num:]
        if b.count(h2) == 0:
            return False
        else:
            return True


# In[3]:


#輸入測試資料
#from Crypto.Hash import MD5
#h = MD5.new()
#h.update("dog".encode("utf-8"))
#print(h.hexdigest())
#print(int(h.hexdigest(),16))
#--------------------------------
a = MyHashSet()
a.add("dog")
a.add("pig")
b = a.contains("pig")
print(b)                      #True
b = a.contains("dog")
print(b)                      #True
b = a.contains("cat")
print(b)                      #False
a.add("bird")
b = a.contains("bird")
print(b)                      #True
a.remove("pig")
b = a.contains("pig")
print(b)                      #False


# In[4]:


#測試是否能刪除相同值
a = MyHashSet()
a.add("dog")
a.add("pig")
a.add("pig")
b = a.contains("dog")
print(b)  
a.remove("pig")
b = a.contains("pig")
print(b)    

