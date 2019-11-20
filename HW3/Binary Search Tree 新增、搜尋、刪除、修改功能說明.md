Binary Search Tree功能說明：
------
<br>
- 新增(放入數值):
1. 首先觀察要放入的值與root的值比較大小
2. 再看原本root的左右邊是否已經有值了
     
<br>     放入的值如果小於等於原來的root
<br>     放入root的左邊
<br>     如果root的左邊有節點了
<br>     與root左節點比較
<br>     如果沒有其他節點
<br>     放入root的左邊
<br>     
<br>     放入的值如果大於原來的root
<br>     放入root的右邊
<br>     如果root的右邊有節點了
<br>     與root右節點比較
<br>     如果沒有其他節點
<br>     放入root的右邊
<br>
<br>     換成以代號顯示
<br>     放入的值:x 原本root:root
<br>     if x < root or x = root
<br>         if root.left = None
<br>             root.left = x
<br>         else
<br>             root.left.insert(x)
<br>     else
<br>         if root.right = None
<br>             root.right = x
<br>         else
<br>             root.right.insert(x)
    
