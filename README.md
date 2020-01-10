## 資料結構與演算法(DSA) - 108/9 ~ 109/1
------

個人簡介：
------
大家好，我是巨資三B 賴祐全，我從國中開始第一次接觸類似程式的環境，有`Scratch`這種不用寫Code而用拚接的方式來讓物體移動或操作，到了高中也嘗試了`Visual Basic`，需要寫Code，慢慢可以自己開始探索"程式"到底是甚麼運作的，也可以自己發想創意，在那時候我有選修程式設計課程，也有參加資料科學社，我成功做出來一個間單的四則運算遊戲，做出來的時候還有在學校社團發表會上給其他人使用，雖然我覺得算是一個簡單的東西，排版和一些設計不是到很好，不過有做到我一開始所想像想做到的功能。
<br>    之後到大學慢慢開始接觸`Java`、`C`、`Python`等等程式語言，在這些語言中要最重要的事情就是找的一個可以專精的用，除此之外，當然也是可以了解其他語言在各自部分都有優點，想是MATLAB就是專門畫圖的，PYTHON對於矩陣以及數學的運算很好用等等。只要領悟了每一個程式語言當中的重點核心觀念，學習多個語言也不是難事了。(當然我還沒領悟...之後體會到了就可以做很多事情了吧。)

課後關於課程簡單心得：
------

<br>本來在剛開始這學期的課程時，我還沒了解老師要我們做的事情，我就也跟著老師說的先去練習CodeSignal以及Leetcode，CodeSignal是給基礎的開始練習的，所以有些題目比較簡單，後面才會開始變難，Leetcode有分三個難度等級，大致上會需要先有一些基礎。
<br>等到一個月的練習期後，之後就開始要自己交出作業來，也要依照格式繳交，當初是大家沒有弄清楚真正的正確格式，後來因為助教和老師跟我們全部修課的學生一起討論格式，大家都互相修正以及溝通，我也開始有信心可以完成往後的作業，之後繳交的作業也有慢慢進入狀況。
<br>總結來說，我認為這堂課學習的核心關鍵是學會有自己解決問題的能力，並不是說每個人對於程式撰寫這方面的是一開始就懂，可以到一個人獨立寫一個小程式，但是我們可以慢慢累積在遇到不會的時候我們可以怎麼處理。像我自己就是會先去上網找資料，學習別人如何思考以及處理，再來用自己的方式來結合不同的功能一起呈現，讓原本可以做到一項呈現可以變成一次呈現多種不同的功能，這也是我想做到的。

<br> >>此Repository(資料集)的內容大致分布如下圖：
<br>![結構圖]()

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

Week2 - Linked List
------
[Linked List 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/blob/master/Content/Linked%20List.py)
###### Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）。
因此，每個節點本身應該要有兩種屬性（attribute），一個是本身帶有的值或者是資料，另一個則是指向下一個節點的指標（pointer）。
Linked-list與一般陣列（array）比起來最大的不同點在於：
陣列使用一連串的記憶體位置，因此可以透過array[index]直接存取資料，但是相對的，若要在陣列中加入或是刪除元素，則需要大量的資料搬移。（python中的list雖然用法跟陣列很類似，並卻不是這樣子的實作方式。而像是在C語言中，陣列所記錄的其實是第一個元素的地址，而index就是相對於第一個元素的偏移量了，所以才是從0開始。）

Week3 - Stack
------
[Stack 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/blob/master/Content/Queue%20%26%20Stack.py)
###### 堆疊(Stack)
加入(push)與刪除(pop)於同一端
<br>具有後進先出(LIFO, Last-in-First-out)或先進後出(FILO, First-in-Last-out)性質的有序串列
<br>例子：疊盤子、發牌、走迷宮

Week4 - Queue
------
[Queue 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/blob/master/Content/Queue%20%26%20Stack.py)
###### 佇列(Queue)
加入(enqueue)與刪除(dequeue)於不同端(front & rear)或先進先出(FIFO, First-in-First-out)
<br>例子：排隊買票、坐公車

Week5 - Set
------
<br>又稱集合，是資料結構的一種，可以用來表達資料中出現的種類有哪些，不會計算重複出現的單一資料，也跟數學的集合有同樣的概念。

<br>作業項目回顧：
<br>問題描述 -> 程式架構設計說明 -> 流程圖 -> 逐步解釋說明 -> 測試值使用範例 -> 其他補充說明

Week6 - Insertion Sort
------
[參考資料](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)
<br>將資料分成已排序、未排序兩部份，依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置
<br>插入時由右而左比較，直到遇到第一個比正處理的值小的值，再插入，比較時，若遇到的值比正處理的值大或相等，則將值往右移
<br>都從第一項開始比，依序往下比到最後一個數，是穩定的結構，但處理排序速度比較慢。

* 這裡所稱的排序(Sorting)，是指將一串不規則的數值資料(陣列資料)依照遞增或是遞減的方式重新編排。要將一串不規則的數值資料遞增或是遞減排列，方法當然不會只有一種，而排序演算法(Sorting Algorithm)就是排列資料的方法。

外部網站連結:
<br>[各種排序法動畫演示](https://www.toptal.com/developers/sorting-algorithms)
<br>[各式演算法教學](https://github.com/TheAlgorithms/Python)
<br>[資料結構與演算法總整理介紹](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)

Week7 - Quick Sort
------
[Quick Sort 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW1)
<br>[參考網站](https://kopu.chat/2017/08/03/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F-quick-sort/)
<br>在數列中隨便找一個數字作為基準 (pivot)，然後把該數列中所有比基準數小的數字都放在左邊、比基準數大的數字都放在右邊。

<br>即代表此陣列已經被切割成左、右兩個子陣列。再讓左右兩個子陣列各自做排序，當左、右子陣列排完時，整個排序也就結束了。
<br>
![Quick Sort](http://www.cs.swarthmore.edu/~soni/cs35/f13/Labs/images/06/quickSort.png)

Week8 - Heap Sort
------
[Heap Sort 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW2)
<br>[參考資料](https://magiclen.org/heap-sort/)
<br>堆積排序有法兩個大步驟：
<br>第一個是把要排序的陣列製作成「最小堆積」(Min Heap)或是「最大堆積」(Max Heap)。
<br>如果要將陣列遞增排序的話就使用最大堆積；如果要遞減排序的話就使用最小堆積。
<br>接下來的步驟就是利用最大堆積和最小堆積來進行排序，方法和建立最大堆積或是最小堆積時是幾乎一樣的。

<br>什麼是完全二元樹？完全二元樹是一種二元樹，它只允許最後一層(最底下那層)的節點數量可以不必填滿(若頂層是第1層，則第n層的最大節點數量為2n-1)。

Week9 - Merge Sort
------
[Merge Sort 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW2)
<br>[參考資料](https://emn178.pixnet.net/blog/post/87965707-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95%28merge-sort%29)
<br>合併排序法(或稱歸併排序法)，是排序演算法的一種，使用Divide and Conquer的演算法來實作。排序時需要額外的空間來處理，過程依照以下步驟進行：

* 將陣列分割直到只有一個元素。
* 開始兩兩合併，每次合併同時進行排序，合併出排序過的陣列。
* 重複2的動作直接全部合併完成。

Week10 - Binary Tree
------
[參考網站](http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html)
<br>「二元樹」是計算機科學最重要的概念，甚至可以說：二元樹開創了計算機科學。

<br>像是排序資料結構`Binary Search Tree`、極值資料結構`Heap`、資料壓縮`Huffman Tree`、3D 繪圖`BSP Tree`，這一大堆稀奇古怪的術語，通通都是二元樹，二元樹的應用相當廣泛。

<br>「二元樹」與「樹」，儘管名稱相近，但是概念不相近，至於用途更是天差地遠，兩者可以分別獨立學習。

Week11 - Binary Search Tree
------
[BST 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW3)
<br>[參考網站](https://medium.com/@Kadai/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E5%A4%A7%E4%BE%BF%E7%95%B6-binary-search-tree-3c40be3204e)
<br>
<br>BST 的四條定義：
<br>1. 以左邊節點 ( left node ) 作為根的子樹 ( sub-tree ) 的所有值都小於根節點 ( root )
<br>2. 以右邊節點 ( right node ) 作為根的子樹 ( sub-tree ) 的所有值都大於根節點 ( root )
<br>3. 任意節點 ( node ) 的左、右子樹也分別符合 BST 的定義
<br>4. 不存在任何鍵值 ( key/value ) 相等的節點。
<br>
<br>可以使用的功能有以下幾點：
<br> >> 新增：加入一個值到BST裡，符合以上四點定義。
<br> >> 刪除：從原本的BST中刪除一個值，刪除後檢查是否符合定義。
<br> >> 查詢：照原本新增的方式去找到要搜尋的值。
<br> >> 修改：結合刪除加上新增兩項功能，修改後也要檢查是否符合BST定義。

Week12 - Red Black Tree
------
[BRT 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/blob/master/Content/Red%20%20Black%20Tree.py)
<br>[參考網站](http://alrightchiu.github.io/SecondRound/red-black-tree-introjian-jie.html)
<br>Red Black Tree(RBT)是node塗了「顏色」的Binary Search Tree(BST)，藉由控制顏色，能夠保證在RBT中，最長path(路徑)不會超過最短path的兩倍(若最短的path是5，最長的path至多只能是10)，如此，RBT便能夠近似地視為平衡。

Week13 - Hash Table
------
[Hash Table 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW4) 
<br>[參考網站](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)
<br>Hash Table 是儲存 (key, value) 這種 mapping 關係的一種資料結構，插入元素、移除元素跟找某個元素大概都只要 O(1) 的時間複雜度。
<br>為什麼他的時間複雜度這麼低呢? 
<br>舉例來說，如果我們有 n 個數字要儲存，一般大家常會用 array 來存。如果我們拿到另一個數字 A，要判斷這個數字 A 有沒有在 array 裡面，那我們勢必得跟 array 裡的元素一個個比較，時間複雜度是 O(n)。(先做過 sorting 的話，就可以用二分搜尋法比較快地找到，但還是需要 O(logn) 的時間複雜度)

<br>但因為 hash function 的關係，如果先把 n 個數字儲存在 Hash Table 裡面，那如果要判斷這個數字 A 是不是已經被存在 Hash Table 裡面，只要先把這個數字丟進 hash function，就可以直接知道 A 對應到 Hash Table 中哪一格。所以其實是 hash function 幫我們省去了一個個比較的力氣。

Week14 - Breadth-First Tree
------
[BFS 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW5)
<br>[參考網站](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html)
<br>BFS(橫向優先搜尋法)是以某一節點為出發點，先拜訪所有相鄰的節點。再依序拜訪與剛才被拜訪過的節點相鄰但未曾被拜訪過的節點，直到所有相鄰的節點都已被拜訪過。 
<>因此，進行BFS時，需要使用queue(先進先出的概念)，以便記錄拜訪的順序。

Week15 - Depth-First Tree
------
[DFS 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW5)
<br>[參考網站](http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html)
<br>深度優先搜尋法，是一種用來遍尋一個樹(tree)或圖(graph)的演算法。
<br>由樹的根或圖的某一點當成根(root)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並盡可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目的節點或遍尋全部節點。

<br>DFS屬於盲目搜索(uninformed search)是利用堆疊(Stack,後進先出的概念)來處理，通常以遞迴的方式呈現。

Week16 - Minimum Spanning Tree
------
[MST - Dijkstra 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW6)
<br>[參考網站](https://www.itdaan.com/tw/bb9aae32a7ecd771ef13c6b43d07f41f)
<br>[參考2](http://alrightchiu.github.io/SecondRound/minimum-spanning-treeintrojian-jie.html)
<br>生成樹：一個連通圖的生成樹，指的是該圖的一個子圖，它包含圖的所有頂點（N個），但只有足夠把所有頂點連接在一起的N-1條邊。 
<br>如果再向其中添加一條邊，那就會有環產生。
<br>最小生成樹：一個連通圖的所有生成樹中，所有邊的權種加起來為最小的生成樹，稱為最小生成樹。

Week17 - Shortest Path
------
[SP - Kruskal 連結](https://github.com/LaiYuChung/108-Data_Structure_and_Algorithm/tree/master/HW6)
<br>[參考網站](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/541508/)
<br>[參考2](http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html)
<br>
* Dijkstra演算法是典型最短路徑演算法，用於計算一個節點到其他所有節點的最短路徑。主要特點是以起始點為中心向外層層擴充套件，直到擴充套件到終點為止。
* Dijkstra演算法能得出最短路徑的最優解，但由於它遍歷計算的節點很多，所以效率低。
* 演算法思考：
* 設G=(V,E)是一個帶權有向圖，把圖中頂點集合V分成兩組，第一組為已求出最短路徑的頂點集合（用S表示，初始時S中只有一個源點，以後每求得一條最短路徑 , 就將 加入到集合S中，直到全部頂點都加入到S中，演算法就結束了），第二組為其餘未確定最短路徑的頂點集合（用U表示），按最短路徑長度的遞增次序依次把第二組的頂點加入S中。在加入的過程中，總保持從源點v到S中各頂點的最短路徑長度不大於從源點v到U中任何頂點的最短路徑長度。此外，每個頂點對應一個距離，S中的頂點的距離就是從v到此頂點的最短路徑長度，U中的頂點的距離，是從v到此頂點只包括S中的頂點為中間頂點的當前最短路徑長度。

Week18 - 總複習 & 期末驗收
------
2020/1/2 今天是期末測驗，在手寫程式碼這方面還要再加強，聽很多人說以前電腦沒有很普及，效能也沒有說很好，只能先自己在紙上先寫好，再一次到電腦上呈現自己的成果，我們活在這個世代越來越方便，每個人幾乎都能自己直接在電腦上測試自己寫的程式是否正確，也可以自己不斷修改直到正確，雖然我們已經有了概念了，但在AFK(Away From Keyboard)的時候可能就沒辦法自己把所想能執行的程式碼寫出來。

