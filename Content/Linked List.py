
# coding: utf-8

# Linked List 實作
# ---
#     

# In[ ]:


class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        self.data = data    # store data
        self.next = None    # store reference (next item)
        return
    
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False
class SingleLinkedList:
    def __init__(self):
        "constructor to initiate this object"
        
        self.head = None
        self.tail = None
        return
    def add_list_item(self, item):
        "add an item at the end of the list"
        
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
            
        return
    def list_length(self):
        "returns the number of list items"
        
        count = 0
        current_node = self.head
        
        while current_node is not None:
            count = count + 1    # increase counter by one            
            current_node = current_node.next    # jump to the linked node
            
        return count
    def output_list(self):
        "outputs the list (the value of the node, actually)"        
         current_node = self.head        
        while current_node is not None:
            print(current_node.data)            
            current_node = current_node.next  # jump to the linked node 
        return


# In[ ]:


#參考資料:https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        current = self.head
        count = 0
    while current:
        count += 1
        current = current.get_next()
    return count
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
        

