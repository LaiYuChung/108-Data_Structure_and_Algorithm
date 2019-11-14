
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

# # Heap Sort Pseusode code
# <br>MaxHeapify(A, i)
# <br>    l = left(i)
# <br>    r = right(i)
# <br>    if l <= heap-size[A] and A[l] > A[i]
# <br>        then largest = l
# <br>    else largest = i
# <br>    if r <= heap-size[A] and A[r] > A[largest]
# <br>        then largest = r
# <br>    if largest != i
# <br>        then swap A[i] with A[largest]
# <br>        MaxHeapify(A, largest)
# <br>end func
# <br>BuildMaxHeap(A)
# <br>    heap-size[A] = length[A]
# <br>    for i = |length[A]/2| downto 1
# <br>        do MaxHeapify(A, i)
# <br>end func
# <br>HeapSort(A)
# <br>    BuildMaxHeap(A)
# <br>    for i = length[A] downto 2
# <br>        do swap A[1] with A[i]
# <br>            heap-size[A] = heap-size[A] – 1
# <br>            MaxHeapify(A, 1)
# <br>end func
# #參考資料:https://www.codingeek.com/algorithms/heap-sort-algorithm-explanation-and-implementation/

# In[65]:


#依照網路上找到的Pseusode code試轉成可執行的code
class Solution2(object):
    def __init__(self):
        self.x = []
    def Maxheapify(x,i):
        left = 2 * i + 1                         #左節點位置
        right = 2 * (i + 1)                      #右節點位置
        if left < len(x) and self.x[left] > self.x[i]:
            largest = left
        else:
            largest = i
        if right < len(x) and self.x[right] > self.x[largest]:
            largest = right
        else:
            largest = i   
        if largest != i:
            self.x[i],self.x[largest] = self.x[largest],self.x[i]     #交換位置
            self.Maxheapify(largest)           
    def heap_sort(self,x):
        length = len(self.x)
        mid = len(self.x)//2 - 1
        for i in range(mid,-1,-1):
            self.Maxheapify(length,i)
        for i in range(length-1,0,-1):
            self.x[i],self.x[0] = self.x[0],self.x[i]
            self.Maxheapify(i,0)
        return x
#目前嘗試轉Pseusode code還是有一些錯誤，回傳值的部分


# In[66]:


y = [4,5,2,7,3,1,19,4]
a = Solution2().heap_sort(y)
a


# In[64]:


class Solution(object):        
    def maxheapify(self,x,n,i):
        left = 2 * i + 1                         #左節點位置
        right = 2 * (i + 1)                      #右節點位置
        largest = i
        if left < n and x[left] > x[i]:
            largest = left
        if right < n and x[right] > x[largest]:
            largest = right  
        if largest != i:
            x[largest],x[i] = x[i],x[largest]  #交換位置
            self.maxheapify(x,n,largest)
            
    def heap_sort(self,x):
        n = len(x)
        for i in range(n,-1,-1):               #從後面往前看
            self.maxheapify(x,n,i)
        for i in range(n-1,0,-1):
            x[i],x[0] = x[0],x[i]              #交換位置
            self.maxheapify(x,i,0)
        return x


# In[65]:


a = [4,7,24,6,3,99,4,0]
a1 = Solution().heap_sort(a)
a1


# In[7]:


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

