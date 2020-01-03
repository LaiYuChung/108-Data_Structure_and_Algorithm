
# coding: utf-8

# In[ ]:


#2020/1/3 
#Dijkstra & Kruskal function
#addEdge 、 Dijkstra 、 Kruskal


# In[ ]:


from collections import defaultdict 

class Graph(object): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.seen = []
        self.edge = []
        self.weight = []
    def addEdge(self,u,v,w):
        self.graph[u].append(v) 
        return
    def to_edge(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j]!=0:
                    connect = [i,j]
                    self.edge.append(connect)
                    self.weight.append(j)
        print(self.edge,"\n",self.weight)
        return
    def Dijkstra(self,s): 
        node = [str(i) for i in range(self.V)]
        cost = self.graph[s]
        self.seen.append(s)
#       for i in range(len(self.V)):
#            self.seen.append(s)
 
        first = dict(zip(node,cost))
        return first

    def get_min(self,arrn):                   #找最小值位置
        small = []
        for i in range(len(self.graph[arrn])):
            if self.graph[arrn][i] == 0:
                pass
            else:
                small.append(self.graph[arrn][i])
        return self.graph[arrn].index(min(small))
    def Kruskal(self):
        pass

