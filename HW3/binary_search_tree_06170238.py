
# coding: utf-8

# In[ ]:


#Binary Search Tree function
#2019/11/22
#function:insert,search,delete,modify


# In[1]:


class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution(object):
    def insert(self,root,val):
        if val <= root.val:                  #放入的數值小於或等於原本的值，放左邊
            if root.left:                    #如果左節點存在，與target的比較由root變為root.left(左節點)
                return self.insert(root.left,val)
            else:
                root.left = TreeNode(val)   #如果還沒有左節點，val為root的左節點
                return root.left
        else:                                #放入的數值大於原本的值，放右邊
            if root.right:                   #如果右節點存在，與target的比較由root變為root.right(右節點)
                return self.insert(root.right,val)
            else:
                root.right = TreeNode(val)  #如果還沒有右節點，val為root的右節點
                return root.right            #回傳value為root的右節點
    def search(self,root,x):
        if root.val > x:
            if (root.left != None) and (root.left.val != x):
                return self.search(root.left,x) 
            elif (root.left != None) and (root.left.val == x):
                return root.left
            else:
                return "Fail to find value"
        elif root.val < x:
            if (root.right != None) and (root.right.val != x): 
                return self.search(root.right,x)
            elif (root.right != None and root.right.val == x):
                return root.right
            else:
                return "Fail to find value"
        elif root.val == x:
            return root
    def adjust_tree(self,root):     #調整為符合tree的格式
        current = root
        if current.left != None:    #如果被刪除的節點底下有兩個子節點
            current = current.left  #先往左邊找下一個左節點為新的root
        return current
    def preorder(self,root):
        if root:
            print(str(root.val))
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)
    def delete(self, root, val):
            #先尋找節點位置
        if val < root.val:
            root.left = self.delete(root.left,val)
        elif val > root.val:
            root.right = self.delete(root.right,val)
        else:
            #要刪除的值底下有一個節點
            if root.left == None:
                new_root = root.right
                root = None
                return new_root
            elif root.right == None:
                new_root = root.left
                root = None
                return new_root
            #要刪除的值底下有兩個節點
            new_root = self.adjust_tree(root.right)
            root.val = new_root.val
            root.right = self.delete(root.right,new_root.val) 
        return root
    def modify(self, root, target, new_val):
        if self.search(root,target) == None:
            return False
        else:
            self.delete(root,target)
            self.insert(root,new_val)


# In[2]:


root = TreeNode(50)
s = Solution()
s.insert(root,70)
s.insert(root,60)
s.insert(root,40)
s.insert(root,30)
print(s.preorder(root))
print("===search===")
print(s.search(root,40))
print(s.preorder(root))
print("===delete===")
print(s.delete(root,40))
print(s.preorder(root))
print("===modify===")
s.modify(root,60,35)
print(s.preorder(root))

