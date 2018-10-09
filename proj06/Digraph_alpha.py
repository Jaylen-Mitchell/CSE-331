import math
from collections import deque


class Digraph:
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        
        self.order = n
        self.size = 0
        self.digraph_struct = [{} for _ in range(n)]
#        print(self.digraph_struct)
        # You may put any required initialization code here
        
            
        
    def does_source_dest_exist(self,s,d):
        if (d> len(self.digraph_struct)) or(s>len(self.digraph_struct)):
            raise IndexError 
        return True
    def neighbors(self,s):
        vertex = self.digraph_struct[s]
        my_neighbor =[(*vertex)]
        my_neighbor.sort()
        return my_neighbor 
    
    def insert_arc(self, s, d, w):
#        print("source",s)
#        print("weight",w)
#        print("dest",d)
        self.does_source_dest_exist(s,d)
        if(self.are_connected(s,d)):
            self.digraph_struct[s][d]=w
            return
        else:
            self.digraph_struct[s][d] = w
            self.size+=1
#            print("Hi",self.digraph_struct[s])
#            print(self.digraph_struct)
#           print("3",self.digraph_struct[3])

    def out_degree(self, v):
        self.does_source_dest_exist(v,d=0)
        return len(self.digraph_struct[v].keys())#Since each key is a dest if we want the number of edegs leaving
                                                #a vertex we just return the numebr of keys in that dictinary for that node
    def are_connected(self, s, d):
        self.does_source_dest_exist(s,d)
        if d in self.digraph_struct[s]:#We check the source(aka the node) if there is a dest to another node 
            return True                #Then the pathway between them proves they are connected! :)
        return False

    def is_path_valid(self, path):
        previous = path[0]
#        print("prev",previous)
        path_len = len(path)
        if path_len == 1:
            return True
        else:
            for i in range(1,len(path)):
                current = path[i]
#                print("curr",current)
                self.does_source_dest_exist(previous,current)
                if self.are_connected(previous,current):
                    previous = current
                    continue
                else:
                    return False
        return True

    def arc_weight(self, s, d):
        if not self.are_connected(s,d):
            return math.inf
        self.does_source_dest_exist(s,d)
        return self.digraph_struct[s][d]

    def path_weight(self, path):
#        self.is_path_valid(path)
        previous = path[0]# Prev will be the first index of path
#        print("prev",previous)
        path_weight = 0
        for i in range(1,len(path)):# We iterate though the path list and check if previous and current have valid paths
            current = path[i]
#            print("curr",current)
            self.does_source_dest_exist(previous,current)#Make sure the vertex's are valid to begin wtih
            if self.are_connected(previous,current):#If a path exisit between them then we add their arc weight
                path_weight+=self.arc_weight(previous,current)
                previous = current#We update previous to be current so that the next iteration previous will be 
            else:                 #one behind current(like a shadow)
                return math.inf#All else we return math.inf if dont get a value for path_weight
        return path_weight

    def does_path_exist(self, s, d):
        self.does_source_dest_exist(s,d)
        if self.are_connected(s,d):
            return True
        else: 
            # Mark all the vertices as not visited
            visited =[False]*(self.order)
            #Init list of neighbors of our source vertex
            my_neighbors =self.neighbors(s)
            # Create a queue for DFS
            deq=deque()
            # Mark the source node as visited and enqueue it
            deq.append(s)
            visited[s] = True
            while deq:
                for neighbor in my_neighbors:
                        if visited[neighbor] == False:#If we haven't seen it, add it to our stack and mark it as seen
                            deq.append(neighbor) 
#                            print(deq)
                            visited[neighbor] = True
                #Dequeue a vertex from queue
                #Once we exhaust our neighbors we pop the top off and check if this was where we wanted to end up
#                print("deq before pop",deq)
                s= deq.pop()#We backtrack and update "s" until we find neighbors we havent seen yet
                if s == d:
                    return True
                my_neighbors = self.neighbors(s)#If this isn't our dest we check through a new list of neighbors 
                continue                        #with our update source veretx "s"
             
            return False
    def find_min_weight_path(self, s, d):
        self.does_source_dest_exist(s,d)#You know the drill... Are they even real vertex's?
        path=[s,d]
        if len(path) != len(set(path)) and len(path)<3:#If we only have two vertex's and their duplicates then
            return[s]                                  #their min path weight will be zero with the path being just 
        elif self.are_connected(s,d):                  # a single instance 
            return path# If they are conncted we will make use of code we already have :)(It will be just their arc weight)
        current_weight=0
        min_weight_lst=[]
        min_weight_path=[s]#Init our min weight path to just include our source
        # Mark all the vertices as not visited
        visited =[False]*(self.order)
#        Init list of neighbors of our source vertex
        my_neighbors =self.neighbors(s)
#        print(my_neighbors)
        # Create a queue for DFS
        deq=deque()
        # Mark the source node as visited and enqueue it
        deq.append(s)
        visited[s] = True
        while deq:
            for neighbor in my_neighbors:
                    current_weight= self.path_weight([s,neighbor])
                    min_weight_lst.append(current_weight)
                    if visited[neighbor] == False:#If we haven't seen it, add it to our stack and mark it as seen
                        deq.append(neighbor) 
                        visited[neighbor] = True
#            print(min_weight_lst)
#            print("before pop",deq)
            if len(min_weight_lst)==0:
                raise ValueError 
            val, idx = min((val, idx) for (idx, val) in enumerate(min_weight_lst))
#            print(idx)
            least_weight_neighbor = my_neighbors[idx]
#            print("least_weight",least_weight_neighbor)
            min_weight_path.append(least_weight_neighbor)
#            print("min path",min_weight_path)
            s= deq.pop()#We backtrack and update "s" until we find neighbors we havent seen yet
#            print(deq)
            if s == d:
                return min_weight_path
            my_neighbors = self.neighbors(least_weight_neighbor)#Cycle through new neighbors
            min_weight_lst.clear()#clear old weight lst of old neighbors weight
            continue
        else:
            raise ValueError 
          
#    def __itr__(self):
#        for item in self.digraph_struct:
#            yield item
#    def pretty_print(self,itr):
#        return list(self, self.__itr__)
        
            

