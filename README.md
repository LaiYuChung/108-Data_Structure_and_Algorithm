## 資料結構與演算法(DSA) - 108/9 ~ 109/1
------

個人簡介：
------
大家好，我是巨資三B 賴祐全，我從國中開始第一次接觸類似程式的環境，有`Scratch`這種不用寫Code而用拚接的方式來讓物體移動或操作，到了高中也嘗試了`Visual Basic`，需要寫Code，慢慢可以自己開始探索"程式"到底是甚麼運作的，也可以自己發想創意，在那時候我有選修程式設計課程，也有參加資料科學社，我成功做出來一個間單的四則運算遊戲，做出來的時候還有在學校社團發表會上給其他人使用，雖然我覺得算是一個簡單的東西，排版和一些設計不是到很好，不過有做到我一開始所想像想做到的功能。
<br>之後到大學慢慢開始接觸Java、C、Python等等程式語言，

課後關於課程簡單心得：
------

<br>本來在剛開始這學期的課程時，我還沒了解老師要我們做的事情，我就也跟著老師說的先去練習CodeSignal以及Leetcode，CodeSignal是給基礎的開始練習的，所以有些題目比較簡單，後面才會開始變難，Leetcode有分三個難度等級，大致上會需要先有一些基礎。
<br>等到一個月的練習期後，之後就開始要自己交出作業來，也要依照格式繳交，當初是大家沒有弄清楚真正的正確格式，後來因為助教和老師跟我們全部修課的學生一起討論格式，大家都互相修正以及溝通，我也開始有信心可以完成往後的作業，之後繳交的作業也有慢慢進入狀況。
<br>總結來說，我認為這堂課學習的核心關鍵是學會有自己解決問題的能力，並不是說每個人對於程式撰寫這方面的是一開始就懂，可以到一個人獨立寫一個小程式，但是我們可以慢慢累積在遇到不會的時候我們可以怎麼處理。像我自己就是會先去上網找資料，學習別人如何思考以及處理，再來用自己的方式來結合不同的功能一起呈現，讓原本可以做到一項呈現可以變成一次呈現多種不同的功能，這也是我想做到的。

<br> >>此Repository(資料集)的內容大致分布如下圖：

課堂作業連結：
------
<br>HW1 - [Quick Sort](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW1)
<br>HW2 - [Merge Sort & Heap Sort](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW2)
<br>HW3 - [Binary Search Tree](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW3) 
<br>HW4 - [Hash Table](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW4) 
<br>HW5 - [BFS & DFS](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW5) 
<br>HW6 - [MST & Shortest Path](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW6)

Week1 - 課程介紹
------
課程主軸分成兩個部分：
<br>1、資料結構(Data Structure):
<br>參考:[資料](https://zh.wikipedia.org/zh-tw/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
* 是電腦中以不同類型儲存、組織資料的方式。
* 不同的設計方式會導致電腦運作速度快慢，好的設計可以減少儲存空間以及時間。
* 以下是常見的資料結構:
<br>

|堆疊(Stack)|佇列(Queue)|陣列(Array)|連結串列(Linked List)|
|:-----:|:-----:|:-----:|:-----:|
|樹(Tree)|圖(Graph)|堆積(Heap)|雜湊表(Hash table)|

<br>2、演算法(Algorithm):
<br>參考:[資料](https://jason-chen-1992.weebly.com/home/-whats-algorithm)

* 簡單來說:
* 用有限步驟所構成的集合，可以用於解決某一個特定的問題。
* 以電腦科學上:
* 透過設計一連串的指令、動作，讓電腦去執行，以便協助我們解決一些特定問題。


<br>CodeSignal 連結: [CodeSignal](https://codesignal.com/)
<br>Leetcode 連結: [Leetcode](https://leetcode.com/)
<br>以上兩個是自行練習撰寫及學習程式的網站，`CodeSignal`為從基礎開始練習，等到有一些基礎後就可以開始嘗試挑戰`Leetcode`的題目。
<br>
<br>

Week2 - Linked List
------
[Linked List 連結]()
###### Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）。
因此，每個節點本身應該要有兩種屬性（attribute），一個是本身帶有的值或者是資料，另一個則是指向下一個節點的指標（pointer）。
Linked-list與一般陣列（array）比起來最大的不同點在於：
陣列使用一連串的記憶體位置，因此可以透過array[index]直接存取資料，但是相對的，若要在陣列中加入或是刪除元素，則需要大量的資料搬移。（python中的list雖然用法跟陣列很類似，並卻不是這樣子的實作方式。而像是在C語言中，陣列所記錄的其實是第一個元素的地址，而index就是相對於第一個元素的偏移量了，所以才是從0開始。）

Week3 - Stack
------
[Stack 連結]()
###### 堆疊(Stack)
加入(push)與刪除(pop)於同一端
<br>具有後進先出(LIFO, Last-in-First-out)或先進後出(FILO, First-in-Last-out)性質的有序串列
<br>例子：疊盤子、發牌、走迷宮

Week4 - Queue
------
[Queue 連結]()
###### 佇列(Queue)
加入(enqueue)與刪除(dequeue)於不同端(front & rear)或先進先出(FIFO, First-in-First-out)
<br>例子：排隊買票、坐公車

Week5 - Set
------
[Set 連結]()
作業項目回顧：
<br>問題描述 -> 程式架構設計說明 -> 流程圖 -> 逐步解釋說明 -> 測試值使用範例 -> 其他補充說明

Week6 - Insertion Sort
------
[Insertion Sort 連結]()

* 這裡所稱的排序(Sorting)，是指將一串不規則的數值資料(陣列資料)依照遞增或是遞減的方式重新編排。要將一串不規則的數值資料遞增或是遞減排列，方法當然不會只有一種，而排序演算法(Sorting Algorithm)就是排列資料的方法。

外部網站連結:
<br>[各種排序法動畫演示](https://www.toptal.com/developers/sorting-algorithms)
<br>[各式演算法教學](https://github.com/TheAlgorithms/Python)

Week7 - Quick Sort
------
[Quick Sort 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW1)

Week8 - Heap Sort
------
[Heap Sort 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW2)

Week9 - Merge Sort
------
[Merge Sort 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW2)

Week10 - Binary Tree
------
[Binary Tree 連結]()

Week11 - Binary Search Tree
------
[BST 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW3)

Week12 - Red Black Tree
------
[BRT 連結]()

Week13 - Hash Table
------
[Hash Table 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW4) 

Week14 - Breadth-First Tree
------
[BFS 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW5)

Week15 - Depth-First Tree
------
[DFS 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW5)

Week16 - Minimum Spanning Tree
------
[MST - Dijkstra 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW6)

Week17 - Shortest Path
------
[SP - Kruskal 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW6)


Week18 - 總複習 & 期末驗收
------
2020/1/2 今天是期末測驗，在手寫程式碼這方面還要再加強，聽很多人說以前電腦沒有很普及，效能也沒有說很好，只能先自己在紙上先寫好，再一次到電腦上呈現自己的成果，我們活在這個世代越來越方便，每個人幾乎都能自己直接在電腦上測試自己寫的程式是否正確，也可以自己不斷修改直到正確，雖然我們已經有了概念了，但在AFK(Away From Keyboard)的時候可能就沒辦法自己把所想能執行的程式碼寫出來。

