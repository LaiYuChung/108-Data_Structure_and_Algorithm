
# coding: utf-8

# Heap Sort 概念 & 方法:
# <br>
# 堆積排序法有兩個大步驟，第一個是把要排序的陣列製作成「最小堆積」(Min Heap)或是「最大堆積」(Max Heap)。
# <br>如果要將陣列`遞增排序`的話就使用`最大堆積`；如果要`遞減排序`的話就使用`最小堆積`。
# <br>接下來的步驟就是利用最大堆積和最小堆積來進行排序
# <br>
# <br>什麼是完全二元樹？完全二元樹是一種二元樹
# <br>它只允許最後一層(最底下那層)的節點數量可以不必填滿
# <br>(若頂層是第1層，則第n層的最大節點數量為2^n-1，第3層的最大節點數量為4個，第1層依序節點數量1,2,4,8)。
# 
# <br>參考資料:https://magiclen.org/heap-sort/
#         
# <br>            Heap Sort
# <br>時間複雜度 : O(n*logn)
# <br>空間複雜度 : O(1)
# 

# `--------------------------------------------`
# <br>最小堆積(Min Heap) 和 最大堆積(Max Heap) 說明:
# <br>Max Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要大：
# <br>(i為他在Heap中的index值)
# <br>
# <br>`value(i)` > `value(2i)`
# <br>`value(i)` > `value(2i+1)`
# <br>
# <br>Min Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要小：
# <br>
# <br>`value(i)` < `value(2i)`
# <br>`value(i)` < `value(2i+1)`
# <br>
# <br>
# <br>參考資料:http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

# In[ ]:


# Heap Sort Pseusode code
MaxHeapify(A, i)
    l = left(i)
    r = right(i)
    if l <= heap-size[A] and A[l] > A[i]
        then largest = l
        else largest = i
    if r <= heap-size[A] and A[r] > A[largest]
        then largest = r
    if largest != i
        then swap A[i] with A[largest]
        MaxHeapify(A, largest)
end func
BuildMaxHeap(A)
    heap-size[A] = length[A]
    for i = |length[A]/2| downto 1
        do MaxHeapify(A, i)
end func
HeapSort(A)
    BuildMaxHeap(A)
    for i = length[A] downto 2
        do swap A[1] with A[i]
            heap-size[A] = heap-size[A] – 1
            MaxHeapify(A, 1)
end func
#參考資料:https://www.codingeek.com/algorithms/heap-sort-algorithm-explanation-and-implementation/


# In[1]:


# 參考老師的程式碼
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i):                           #建立堆，給予三個變數(陣列,heap的大小,樹根值為i)
    largest = i # Initialize largest as root      #設定樹根的值(第i個index) 
    l = 2 * i + 1    # left = 2*i + 1             #左節點為2i+1
    r = 2 * i + 2    # right = 2*i + 2            #右節點為2i+2

    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]:       #查看左子節點是否存在且大於樹根的值
        largest = l                     #將此子節點設為新的樹根值

    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: #查看左子節點是否存在且大於樹根的值
        largest = r                     #將此子節點設為新的樹根值

    # Change root, if needed 
    if largest != i:                    #如果不相等
        arr[i],arr[largest] = arr[largest],arr[i] # swap #交換位置

        # Heapify the root. 
        heapify(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr)                   #n等於陣列長度

    # Build a maxheap. 
    for i in range(n, -1, -1): #創建一個根部為最大，依序往下越來越小的堆
        heapify(arr, n, i) 

    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]) 
# This code is contributed by Mohit Kumra 


# In[2]:


#參考資料:https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort
def swap(i, j):                    
    sqc[i], sqc[j] = sqc[j], sqc[i]    #設定交換位置的function

def heapify(end,i):                      #end:陣列長度  i:index
    l = 2 * i + 1                        #左節點位置
    r = 2 * (i + 1)                      #右節點位置
    max = i                              #根節點為第i的位置
    if l < end and sqc[i] < sqc[l]:      
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort():     
    end = len(sqc)                               #陣列長度
    start = end // 2 - 1                       # use // instead of /   
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   

sqc = [2, 7, 1, -2, 56, 5, 3]
heap_sort()
print(sqc)


# In[3]:


a = [2,4,5,6,7,3,8]
b = len(a)
for i in range (b,0,-1):
    print(i)


# In[7]:


# Heap Sort code
class Solution(object):
    def __init__(self,x):
        self.x = x
    def swap(a,b):
        x[a], a[b] = x[b], x[a]        
    def buildheap(n,i):
        root = i
        left = 2*i + 1
        right = 2*i + 1
        
        if left < n and x[n] < x[left]:
            n = left
        if right < n and x[n] < x[right]:
            n = right
        if root != i:
            swap(i,root)
            buildheap(n,root)
    def heap_sort(x):
        n = len(x)
        first = n // 2
        for i in range(n,1):
            buildheap(n,i)
        for i in range(n-1):
            swap(i,0)
            buildheap(i,0)
        return x
    


# In[10]:


y = [4,5,2,7,3,1,19,4]
a = Solution.heap_sort(y)
a

