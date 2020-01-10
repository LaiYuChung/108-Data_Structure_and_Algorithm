
# coding: utf-8

# Red-Black Tree
# ------
# 
# <br>紅黑樹特徵:
# *    (1)每個節點是紅或黑
# *    (2)Root必為黑色
# *    (3)節點紅色，子節點必為黑色
# *    (4)節點黑色，子節點可紅可黑
# *    (5)空節點(Null)為黑色
# *    (6)Root到每個leaf的路徑有相同數目的黑色節點
# 
# <br>平衡:
# *    子節點沒有滿兩個，不能往下一層放
# *    旋轉

# In[ ]:


#Presudo code
#right rotate
Node x = h.left
h.left = x.right
x.right = h
x.color = x.right.color
x.right.color = red
return x


# In[ ]:


class Red_Black_Tree
def search
def insert
def delete
def modify
def left_rotate
def right_rotate
def color


# In[ ]:


#參考:https://leetcode.com/problems/find-median-from-data-stream/discuss/74134/both-ologn-red-black-tree-solution-in-python

class RedBlackTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.isRed = True


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def sizeOf(self, node):
        return node.size if node else 0

    @property
    def size(self):
        return self.sizeOf(self.root)

    def rotateLeft(self, root):
        right = root.right

        root.size, right.size = self.sizeOf(
            root.left) + self.sizeOf(right.left) + 1, root.size

        root.right = right.left
        right.left = root

        right.isRed = root.isRed
        root.isRed = True

        return right

    def rotateRight(self, root):
        left = root.left

        root.size, left.size = self.sizeOf(
            root.right) + self.sizeOf(left.right) + 1, root.size

        root.left = left.right
        left.right = root

        left.isRed = root.isRed
        root.isRed = True

        return left

    def flipColor(self, root):
        root.left.isRed = False
        root.right.isRed = False
        root.isRed = True
        return root

    def insertTo(self, root, val):
        if not root:
            return RedBlackTreeNode(val)

        if val > root.val:
            root.right = self.insertTo(root.right, val)
        else:
            root.left = self.insertTo(root.left, val)

        if (root.right and root.right.isRed) and not (
                root.left and root.left.isRed):
            root = self.rotateLeft(root)

        if (root.left and root.left.isRed) and (
                root.left.left and root.left.left.isRed):
            root = self.rotateRight(root)

        if (root.left and root.left.isRed) and (
                root.right and root.right.isRed):
            root = self.flipColor(root)

        root.size = sum(map(self.sizeOf, (root.left, root.right))) + 1
        return root

    def insert(self, val):
        self.root = self.insertTo(self.root, val)
        self.root.isRed = False

    def searchK(self, k, root=None):
        root = root or self.root

        size = self.sizeOf(root.left) + 1
        if k == size:
            return root.val

        return self.searchK(k, root.left) if k < size else self.searchK(
            k - size, root.right)


class MedianFinder(object):
    def __init__(self):
        self.tree = RedBlackTree()

    def addNum(self, num):
        self.tree.insert(num)

    def findMedian(self):
        size = self.tree.size
        if size & 1:
            return self.tree.searchK(size + 1 >> 1)
        return sum(map(self.tree.searchK, (size >> 1, size + 2 >> 1))) / 2.0

