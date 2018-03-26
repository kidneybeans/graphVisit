# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:04:06 2017

@author: LiuWei
"""

import numpy as np
import random

neighbor = np.zeros((2,8), int)
neighbor[0,:3] = -1
neighbor[0,3:5] = 0
neighbor[0,5:] = 1
neighbor[1,0] = -1
neighbor[1,1] = 0
neighbor[1,2] = 1
neighbor[1,3] = -1
neighbor[1,4] = 1
neighbor[1,5] = -1
neighbor[1,6] = 0
neighbor[1,7] = 1

temp = neighbor[:,0]
neighbor[:,0] = neighbor[:,7]
neighbor[:,7] = temp

class Graph:

    def __init__(self, row, col):
        self.Row = row
        self.Col = col
        self.graph = np.zeros((row,col), int)
        self.visit = np.zeros((row,col), int)
        self.path = []
        self.ok = 0
        
    def setGraph(self, rate):
        #shurow = random.shuffle(random.randint(0,self.Row))
        #shucol = random.shuffle(random.randint(0,self.Col))
        
        #shurow = random.sample(list(np.arange(self.Row)), self.Row)
        shurow = np.arange(self.Row)
        #for i in range(int(self.Row*rate)):
        for i in range(self.Row):
            shucol = random.sample(list(np.arange(self.Col)), self.Col)
            for j in range(int(self.Col*rate)):
                self.graph[shurow[i]][shucol[j]] = 1

    def search(self, startx, starty, endx, endy):
        if self.ok or (startx == endx and starty == endy):
            self.ok = 1
            return self.path
        
        if self.graph[starty][startx] == 1 or starty >= self.Row or startx >= self.Col or \
           starty < 0 or startx < 0:
            return 
        
        visitNum = 0
        for i in range(8):
            if self.ok == 0:
                if starty+neighbor[0][i] >= self.Row or startx+neighbor[1][i] >= self.Col or \
                    starty+neighbor[0][i] < 0 or startx+neighbor[1][i] < 0:
                    continue
                
                if self.visit[starty+neighbor[0][i]][startx+neighbor[1][i]] == 0:
                    visitNum = visitNum + 1
                    if self.graph[starty+neighbor[0][i]][startx+neighbor[1][i]] == 0:
                        self.visit[starty+neighbor[0][i]][startx+neighbor[1][i]] = 1
                        self.path.append([starty+neighbor[0][i],startx+neighbor[1][i]])
                        self.search(starty+neighbor[0][i], startx+neighbor[1][i], endx, endy)
                    else:
                        pass
                else:
                    continue
            
        if self.ok == 0:
            if visitNum == 0:
                if len(self.path) > 0:
                    self.path.pop()
        else:
            return self.path
            

        
testGraph = Graph(8,8)
testGraph.setGraph(0.2)
testGraph.graph[5][5] = 0
testGraph.graph[7][7] = 0
result = testGraph.search(5,5,7,7)
print('graph:', testGraph.graph)
print('result:', result)
print('visit:', testGraph.visit)



