
# coding: utf-8

# In[ ]:


#Breadth-First Search function
#2019/12/16
#function:BFS,DFS


# In[1]:


#參考資料:自己思考步驟並傳換為程式碼
#pair programming 討論

from collections import defaultdict 
class Graph:
    def __init__(self):  
        self.graph = defaultdict(list)  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        return
    def max_length(self):
        return len(self.graph.keys())
    def print_dict(self):
        return self.graph 
    def BFS(self, s): 
        state_1 = []
        state_2 = []
        state_2.append(s)
        index = 0
        while len(state_2) != self.max_length():
            for i in self.graph[s]:
                if state_1.count(i)==0 and state_2.count(i)==0:
                    state_1.append(i)
                else:
                    pass
            state_2.append(state_1[0])
            state_1.pop(0)
            index = index+1
            s = state_2[index]
        return state_2
    
    def DFS(self, s):
        state_1 = []
        state_2 = []
        state_2.append(s)
        while len(state_2) != self.max_length():
            for i in self.graph[s]:
                if state_1.count(i)==0 and state_2.count(i)==0:
                    state_1.append(i)
                else:
                    pass
            state_2.append(state_1[-1])
            s = state_1[-1]
            state_1.pop(-1)
        return state_2

