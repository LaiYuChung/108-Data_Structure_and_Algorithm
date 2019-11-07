
# coding: utf-8

# Merge Sort 概念 & 方法:
# 
# <br>1.將一個`array` 切割成兩個部分 `array1` 和 `array2`
# <br>2.並創造一個新的空`array3`
# <br>3.用前兩個`array1` `array2`的第一項比較
# <br>4.比較小的值放到`array3`
# <br>5.被移動數值所在的`array`往下一個數值去跟原本沒被移動數值的array比較
# <br>6.直到`arrar1` `array2`的所有值都比完
# <br>7.新的`array3`為排序完成的陣列
# 
# <br>            Merge Sort   
# <br>時間複雜度 : `O(n*logn)`  
# <br>空間複雜度 : `O(n)`         

# In[ ]:


# Merge Sort Pseusode code

i,j,m = 0

if (L[i]<=R[j])    #若左右邊數值相同，先放入左邊數字
    M[m]=L[i]
    i++
    m++
elif (L[i]>R[j])
    M[m]=L[i]
    j++
    m++
if i>len(L)
    M.append(R[j:])
elif j>len(R)
    M.append(L[i:])


# In[ ]:


#參考資料:https://stackoverflow.com/questions/18761766/mergesort-with-python

def msort(x):
    result = []
    if len(x) < 2:                        #長度為0,1直接回傳值
        return x
    mid = int(len(x)/2)                   #中間分隔值的index
    y = msort(x[:mid])                    # y為左邊數列
    z = msort(x[mid:])                    # z為右邊數列
    while (len(y) > 0) or (len(z) > 0):   # y或z長度皆大於0進入迴圈
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result

msort([2,6,4,8,2,9])


# 1.先把所有的數字分成兩堆
# <br>2.兩堆的數字再繼續分成更小堆的數字
# <br>3.到最後兩兩數字比大小並排序
# <br>4.直到合成為兩堆各自以排序好的數列
# <br>5.從兩堆第一個數字依序比較放入新的以排序的陣列
# <br>6.兩堆的數字放完即為排序後的數列
# 

# In[ ]:


# Merge Sort code

def merge_sort(x):
    if len(x) <= 1:
        return x
    middle = len(x)//2
    left = merge_sort(x[:middle])
    right = merge_sort(x[middle:])
    a = 0
    b = 0
    i = 0
    final = []
    
    while a < len(left) and  b < len(right):
        if left[a] < right[b]:                 #如果左邊的值小於等於右邊
            final.append(left[a])              #左邊值加入結果列(相等會先加入左邊值)
            a+=1                               #左邊列移到下一項
        else:                                  #如果右邊的值小於或等於左邊
            final.append(right[b])             #右邊值加入結果列
            b+=1                               #右邊列移到下一項
    while a < len(left):
        final.append(left[a])                  #結果列加上左邊數列
        a+=1
    while b < len(right):
        final.append(right[b])                 #反之，結果列加上右邊數列
        b+=1
    return final
 
import random 
alist = []
for i in range(1,random.randint(1,9)):
    alist.append(random.randint(1,100))   #隨機變數創造陣列
print(alist)   
print(merge_sort(alist))


# In[ ]:


疑問: 
函式自己呼叫自己的程序


# In[7]:


# class 作法
class Solution(object):
    def merge_sort(self, x):
        self.x = x
        if len(x) <= 1:
            return x
        middle = len(x)//2
        left = Solution().merge_sort(x[:middle])
        right = Solution().merge_sort(x[middle:])
        a = 0
        b = 0
        i = 0
        final = []

        while a < len(left) and  b < len(right):
            if left[a] < right[b]:                 #如果左邊的值小於等於右邊
                final.append(left[a])              #左邊值加入結果列(相等會先加入左邊值)
                a+=1                               #左邊列移到下一項
            else:                                  #如果右邊的值小於或等於左邊
                final.append(right[b])             #右邊值加入結果列
                b+=1                               #右邊列移到下一項
        while a < len(left):
            final.append(left[a])                  #結果列加上左邊數列
            a+=1
        while b < len(right):
            final.append(right[b])                 #反之，結果列加上右邊數列
            b+=1
        return final
    


# In[9]:


Solution().merge_sort([4,49,16,1,2,64,100,225,169])

