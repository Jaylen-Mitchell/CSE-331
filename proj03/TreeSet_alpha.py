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

    def insert(self,item):
        if(self.root_ == None ):
            return self.insert_root(item)
            
        elif(self.root_ != None):#Once we insert the first eleement we call upon insert helper to insert additional items
            return self.insert_helper(item,self.root_)
        else:
            return False
            
    def remove(self, item):
        if(self.root_ != None):
            return self.remove_helper(item,self.root_)
    def __contains__(self, item):
        if not(self.find(item)):
            return False
        else:
            if(self.find(item)):
                return True

    def first(self):
        if(self.is_empty()):
            raise KeyError
        current_node = self.root_
        while (current_node.left != None):
            current_node = current_node.left
        return current_node.data
    
    
    def last(self):
        if(self.is_empty()):
            raise KeyError
        current_node = self.root_
        while (current_node.right != None):
            current_node = current_node.right
        return current_node.data
    

    def clear(self):
            self.root_ = None
            self.size_ =0
            self.heihgt = -1
            return True
    def __iter__(self):
        return self.inorder(self.root_)
            
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
    def remove_helper(self, item, node):
        if node is None:
            node = self.find(item)#return the node to be deleted

		#root has no parent node	
#        if self.root_.data == node.data: #if it is root
#            parent_node = self.root_
#		'''case 1: The node has no chidren'''
        if node.left is None and node.right is None:
            if item <= node.data:
                node.left = None
            else:
                node.right = None
                return

#		'''case 2: The node has children'''
#		''' if it has a single left node'''
        if node.left is not None and node.right is None :
            if node.left.key < parent_node.key : 
                parent_node.left = node.left
            else:
                parent_node.right = node.left
                return

#		'''if it has a single right node'''
        if node.right is not None and node.left is None:
            if node.key <= parent_node.key:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
                return

#		'''if it has two children'''
#		'''find the node with the minimum value from the right subtree.
#		   copy its value to thhe node which needs to be removed.
#		   right subtree now has a duplicate and so remove it.'''
#        if node.left is not None and node.right is not None:
#            min_value = self.find_minimum(node)
#            node.key = min_value.key
#            min_value.parent.left = None
#            return
            
    def find(self, item):
        if(self.root_ != None):
            return self.find_helper(item, self.root_)
        else:
            return False 

    def find_helper(self, item, node):
        if(item == node.data):
            return node
        elif((self.comp(node.data,item) > 0) and node.left != None):
            return self.find_helper(item, node.left)
        elif((self.comp(node.data,item) < 0)and node.right != None):
            return self.find_helper(item, node.right)
        else:
            return False
        
    def insert_root(self, item):
        if(self.root_ == None):#Check if root Node is intially empty
            self.root_ = TreeNode(item)#insert first root item
            self.size_+=1
            return True
        else:
            return False
    def insert_helper(self,item,node):
        if(self.comp(node.data,item) > 0):
            if(node.left != None):#We recursively call insert helper  starting witht the root nonede passing in a new node as the arguement 
                return self.insert_helper(item,node.left)#along with the same item Until we find a node whos left child has free slot to insert a new node 
            else:
                node.left = TreeNode(item)#If we get here we found a left child who was all alone  and we can insert a new node there! Yay :)
                self.size_+=1
                return True
        elif (self.comp(node.data,item) <0):
            if(node.right != None):
                return self.insert_helper(item,node.right)
            else:
                node.right = TreeNode(item)
                self.size_+=1
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
        # added stuff below

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)
  

