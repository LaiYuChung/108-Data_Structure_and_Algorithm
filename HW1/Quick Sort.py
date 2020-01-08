
# coding: utf-8

#     快速排序(Quick Sort)作法：
#     選定一個基準值(Pivot)
#         >>將比基準值(Pivot)小的數值移到基準值左邊，形成左子串列
#         >>將比基準值(Pivot)大的數值移到基準值右邊，形成右子串列
#         >>分別對左子串列、右子串列作上述三個步驟 ⇒ 遞迴(Recursive)
#     直到左子串列或右子串列只剩一個數值或沒有數值

#     邏輯方法思考:
#     1.先將基準值設為該陣列的中位數
#     2.所有陣列中的數字與基準值做比較
#     3.比較大的移動到基準值的右邊
#     4.比較小的移動到基準值的左邊
#     5.比基準值大的和小的都各重複1~4步驟
#     6.直到所有子串列都只剩一個數字，結果為已排序後的陣列
# 

# In[10]:


#先讀看看別人的做法，思考可以如何減少處理時間

def quicksort(x):
    if len(x) == 1 or len(x) == 0:     #list中若長度為 0 或 1，直接回傳list
        return x
    else:
        pivot = x[0]                   #起始值為第一項
        i = 0
        for j in range(len(x)-1):      #用基準點去跟陣列的其他數字做比較，所以只需要跑陣列長度-1次
            if x[j+1] < pivot:         #因為是以第一項為基準值，所以從第二項開始比較
                x[j+1],x[i+1] = x[i+1], x[j+1]     #如果比基準值小，就與基準值換位置(放到左邊)
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part #把基準值兩邊的數字合併
    
import random 
alist = []
for i in range(1,random.randint(1,9)):
    alist.append(random.randint(1,100))   #隨機變數創造陣列
print(alist)   
print(quicksort(alist))


# In[36]:


#修改基準值為該陣列的中位數

def quicksort(x):
    import numpy as np
    if len(x) <=1 :     #list中若長度小於等於 1，直接回傳list
        return x
    else:
        pivot = np.median(x)                   #起始值為該陣列的中位數
        i = 0
        for j in range(len(x)-1):      #用基準點去跟陣列的其他數字做比較，所以只需要跑陣列長度-1次
            if x[j+1] < pivot:         #因為是以第一項為基準值，所以從第二項開始比較
                x[j+1],x[i+1] = x[i+1], x[j+1]     #如果比基準值小，就與基準值換位置(放到左邊)
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])          #第一區的數字放到基準值的左邊
        second_part = quicksort(x[i+1:])       #第二區的數字放到基準值的右邊
        first_part.append(x[i])                #把基準值加回來陣列中
        return first_part + second_part        #合併兩邊的數字
    
import random 
alist = []
for i in range(1,random.randint(1,9)):
    alist.append(random.randint(1,100))   #隨機變數創造陣列
    
print(alist)   
print(quicksort(alist))


# In[41]:


import numpy as np
x1 = [1,9,8,17,6,4,2]
pivot = np.median(x1)
i = np.where(pivot)

print(pivot)
print(i)


# In[ ]:


#insertion sort
#http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php


# In[23]:


def insertion_sort(arr):
    for i in range(len(arr)-1):
        for k in range(len(arr)-1):
            if arr[k+1] > arr[i]:
                pass
            else:
                arr[i],arr[k+1] = arr[k+1],arr[i]
        arr[i] = arr[k+1]
    return arr


# In[24]:


arr = [72,71,15,70,79,62,79,13,88,1]
insertion_sort(arr)

