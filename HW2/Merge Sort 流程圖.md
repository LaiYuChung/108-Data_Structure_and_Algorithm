Merge Sort 流程:
------

<br>![image](https://github.com/LaiYuChung/DSA_leetcode-project/blob/master/image/merge_sort1.jpg)
<br>這邊我在做的時侯一直卡在`list out of range`
<br>之後我發現判斷式的地方沒有判斷到兩邊的數字相等的情況
<br>原本是寫成`if` `elif`判斷兩邊數字的大
<br>if `右邊` < `左邊`
<br>新list append 右邊的數
<br>右邊`index` `+1`
<br>
<br>elif `左邊` > `右邊`
<br>新list append 左邊的數
<br>左邊`index` `+1`
<br>
<br>這邊就會發生一個錯誤
<br>因為沒有處理到相等的情況
<br>所以之後發現後就改為if else
<br>就能處理全部情況了
<br>
<br>![image](https://github.com/LaiYuChung/DSA_leetcode-project/blob/master/image/merge_sort2.jpg)
<br>再來是處理有一邊的數字已經放完而另一邊還沒放玩數字
<br>這個迴圈會先把上面的跑過一次後再到這個迴圈
<br>如果是a比左邊數列的長度還小(表示左邊數列還沒放完)
<br>就把左邊數列append進去
<br>因為左右邊的數列已經排序過了
<br>所以可以直接放進去
<br>下一個右邊也是一樣的方式
<br>最後就可以輸出結果了
<br>
<br>![image](https://github.com/LaiYuChung/DSA_leetcode-project/blob/master/image/merge_sort3.jpg)

<br>這是全部程式的樣子
===


