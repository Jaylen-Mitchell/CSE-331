class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """
    def __init__(self,comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """
        self.size_= 0
        self.height_ =-1
        self.root_ = None
        self.comp = comp
        # added stuff below
    def getRoot(self):
        return self.root_

    def __len__(self):
        return self.size_

    def height(self):
        return self.height_
    def height_update(self,t):
        if t == None:
            return -1
        else:
            return 1 + max(self.height_update(t.left),self.height_update(t.right))

    def insert(self,item):
        if(self.root_ == None ):
            return self.insert_root(item)
            
        elif(self.root_ != None):#Once we insert the first eleement we call upon insert helper to insert additional items
            return self.insert_helper(item,self.root_)
        else:
            return False
            
    def remove(self, item):
            return self.remove_helper(item,self.root_,None)
    def __contains__(self, item):
        return self.find_helper(item,self.root_)#call recurive find_helper function

    def first(self):
        if(self.is_empty()):
            raise KeyError
        current_node = self.root_
        while (current_node.left != None):#Traverse down left side until we hit min value
            current_node = current_node.left
        return current_node.data
    
    
    def last(self):
        if(self.is_empty()):#Traverse down right side until we hit max value
            raise KeyError
        current_node = self.root_
        while (current_node.right != None):
            current_node = current_node.right
        return current_node.data
    

    def clear(self):
            self.root_ = None#Let garabge collector handle it
            self.size_ =0
            self.heihgt = -1
            return True
    def __iter__(self):
        return self.inorder(self.root_)#call helper function
            
    # Pre-defined methods

    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    # Helper functions
    # You can add additional functions here
#    def logical_successor(self,node):
#        node = node.right
#        if node != None: # just a sanity check  
#            
#            while node.left != None:
#                if node.left == None: 
#                    return node 
#                else: 
#                    node = node.left
#        return node.data

        
    def inorder(self,node):
        if node == None:
            return [] 
        
        inlist = [] 
        l = self.inorder(node.left)#Node pointers
        for i in l:#Visit left side
            inlist.append(i) 

        inlist.append(node.data)#Visit root

        l = self.inorder(node.right)#Node pointes
        for i in l:#Visit right side
            inlist.append(i) 
    
        yield from inlist
    def remove_helper(self, item, node,parent):
        if(node is None):
            return False
        elif(self.comp(item, node.data)==-1):#Recursive visit left side
            return self.remove_helper(item, node.left, node)
        
        elif(self.comp(item, node.data)==1):
            return self.remove_helper(item, node.right, node)#Recursive visit right side
        
        elif(self.comp(item, node.data)==0):
            if (not node.right):
                if (parent is None):
                    self.root_ = node.left
                elif(node is parent.left):
                    parent.left = node.left
                else:
                    parent.right = node.left
                self.size_-=1
                return True
            if not (node.left):
                if (parent is None):
                    self.root_ = node.right
                elif (node is parent.left):
                    parent.left = node.right
                else:
                    parent.right = node.right
                self.size_-=1
                return True
            else:
                temp = node.right
                mini = temp.data
                while(temp.left):
                    temp = temp.left
                    mini = temp.data
                node.data =mini
                return self.remove_helper(node.data, node.right, node)
                
                    
        return False 
    

    def find_helper(self, item, node):
        if(node is None):
            return False
#        if(item == node.data):
#            return True
        elif(self.comp(item,node.data) ==0):
            return True
        elif(self.comp(item,node.data) == 1):
            if (node.right != None):
                return self.find_helper(item, node.right)#Recursive visit right side
        elif (self.comp(item,node.data) == -1):
            if (node.left != None):
                return self.find_helper(item, node.left)#Recursive visit left side
        return False
        
    def insert_root(self, item):
        if(self.root_ == None):#Check if root Node is intially empty
            self.root_ = TreeNode(item)#insert first root item
            self.size_+=1
            self.height_ = self.height_update(self.root_)
            return True
        else:
            return False
    def insert_helper(self,item,node):
        if(self.comp(node.data,item) > 0):
            if(node.left != None):#We recursively call insert helper  starting witht the root nonede passing in a new node as the arguement 
                return self.insert_helper(item,node.left)#along with the same item Until we find a node whos left child has free slot to insert a new node 
            else:
                node.left = TreeNode(item)#If we get here we found a left child who was all alone  and we can insert a new node there! Yay :)
                node.left.parent = node
                self.size_+=1
                self.height_ = self.height_update(self.root_)
                return True
        elif (self.comp(node.data,item) <0):
            if(node.right != None):
                return self.insert_helper(item,node.right)
            else:
                node.right = TreeNode(item)
                node.right.parent = node
                self.size_+=1
                self.height_ = self.height_update(self.root_)
                return True
        else:
            return False
    def natural_order(x, y):
        if x == y:
            return 0
        elif x < y:
            return -1
        else:
            return 1
    

class TreeNode:
    """
    A TreeNode to be used by the TreeSet
    """
    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None
        self.parent = None 
        # added stuff below

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)
  

