class Deque:
    """
    A double-ended queue implemented using a Circular Array
    """
    

    def __init__(self):
        """
        Initializes an empty Deque
        """
        #Data Members
        print("Hello I am a Circular Array Deque, What is it that you require?")
        self.capacity_=4
        self.size_ =0
        self.data_ = [None]*self.capacity_#Arry
        self.front_ = -1
        self.back_ = 0


    
    #Things to note if the last item we push is pushed by "Push_front"
    #Then we need to use resize front which will reset front to be back at -1
    def resize_front(self):
         old_data = self.data_#Store data_'s content into a temp variable 
         self.capacity_*=2
         new_data_ = [None] *self.capacity_#Initilze a new data_ stucture with double the capacity 
         for k in range(0,len(old_data)):
             new_data_[k] = old_data[self.front_+k]#Copy over previous elements back into the newly doubled data_
         self.data_ = new_data_
         self.front_= -1#Re init front to start at the last index(Aka the top)
         self.back_ = self.size_-1#Place the back at the first index(Aka the bottom)
    #If the last item we push is pushed by push_back then we need to use resize_back and reset front to be at the start since we will copy starting from self.front into the new arry
    def resize_back(self):
         old_data = self.data_#Store data_'s content into a temp variable 
         self.capacity_*=2
         new_data_ = [None] *self.capacity_#Initilze a new data_ stucture with double the capacity 
         for k in range(0,len(old_data)):
             new_data_[k] = old_data[self.front_+k]#Copy over previous elements back into the newly doubled data_
         self.data_ = new_data_
         self.front_=0#Re init front to start at the starting index(Aka the top) since we are copying starting from self.front k
                     #into the new arry starting at its first index. We do this to keep the order
         self.back_ = self.size_-1#Place the back at the first index

    def __len__(self):
        """
        Computes the number of elements in the Deque
        :return: The logical size of the Deque
        """
        return self.size_

    def peek_front(self):
        """
        Looks at, but does not remove, the first element
        :return: The first element
        """
        if ((self.is_empty()) or self.data_[self.front_]== None): #If we trip this if block we raise an error since we know the deque should be empty 
            raise IndexError
        return self.data_[self.front_]
                         
    def peek_back(self):
        """
        Looks at, but does not remove, the last element
        :return: The last element
        """
        if ((self.is_empty()) or self.data_[self.back_]== None):#If we trip this if block we raise an error since we know the deque should be empty 
            raise IndexError
        return self.data_[self.back_]
        

    def push_front(self, e):
        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        """
        if(self.size_ >= self.capacity_):#If our Deque is full we need to resize it first
            self.resize_front()
            self.data_[self.front_]= e#New Front
            self.size_+=1
           # print("Case 1")
        elif(self.front_ == -1 and self.size_ ==0) :#If the Deque is intially empty then when we add the first item that will be both the front and the back 
            self.front_= 0
            self.back_ = 0
            self.data_[self.front_]= e #Inserting First element in deque either front end or rear end they both lead to the same result.
            self.size_+=1
           # print("Case 2")
        elif (self.front_ ==0):#If the front is at the beginning of the Deque.This may happen after the first insertion.
            self.front_-=1
            self.data_[self.front_] = e
            self.size_+=1
           # print("Case 3")
        else:
            self.front_ -=1 #We add normally 
            self.data_[self.front_] = e
            self.size_+=1
            #print("Case 4")
            
    def push_back(self, e):
        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        """
        if(self.size_ >= self.capacity_):#If our Deque is full we need to resize it first
            self.resize_back()
            self.back_+=1
            self.data_[self.back_]= e
            self.size_+=1
            #print("case 1")
        elif (self.front_ == -1 and self.size_==0):#If the Deque is intially empty then when we add the first item that will be both the front and the back 
            self.front_= 0
            self.back_=0
            self.data_[self.back_]= e
            self.size_+=1
        else:#The Back is not at the first index(possibly somewhere in between) and if we push back  it we have to go up by one to move to the new back
            self.back_+=1
            self.data_[self.back_] =e 
            self.size_+=1
    def pop_front(self):
        """
        Removes and returns the first element
        :return: The (former) first element
        """
        if (self.is_empty()):
            raise IndexError
        elif(self.front_ == self.back_):#Case where there is only one element in Deque so if we pop it we need to reassign front and back
            first_elm =self.data_[self.front_]#Store first element before we remove it 
            self.data_.remove(self.data_[self.front_])
            self.front_ =-1
            self.back_  =-1
            self.size_  -=1
            return first_elm
        elif(self.front_ ==-1):#Front is at last index and we need to wrap around the circle to reposition the new front 
            first_elm = self.data_[self.front_]
            self.data_.remove(self.data_[self.front_])
            self.front_=0#We reposition front to be at the starting index to account for the wrap around
            self.size_-=1
            return first_elm
        elif(self.front_ ==0 and self.size_!=0):#Front is at last index and we have more than one item sp we need to wrap around the circle to reposition the new front 
            first_elm = self.data_[self.front_]
            self.data_.remove(self.data_[self.front_])
            self.front_=0#We reposition front to be at the starting index
            self.size_-=1
            return first_elm
        else:#The front is not at the last index(possibly somewhere in between) and if we pop it we have to go up by one for the new front
           first_elm = self.data_[self.front_]
           self.data_.remove(self.data_[self.front_])
           self.front_+=1
           self.size_-=1
           return first_elm
           
    def pop_back(self):
        """
        Removes and returns the last element
        :return: The (former) last element
        """
        if(self.is_empty()):
            raise IndexError
        elif(self.front_ == self.back_ and self.size_>1):##Case where there is only one element in Deque so if we pop it we need to reassign front and back
            last_elm =self.data_[self.back_]#Store last element before we remove it 
            self.data_.remove(self.data_[self.back_])
            self.front_ =-1
            self.back_  =-1
            self.size_  -=1
            return last_elm
        elif(self.back_ == 0):#Back is at last index and we need to wrap around the circle to reposition the new front 
            last_elm = self.data_[self.back_]
            self.data_.remove(self.data_[self.back_])
            self.back_-=1#We reposition front to be at the starting index to account for the wrap around
            self.size_-=1
            return last_elm
        elif(self.back_==-1 and self.size_>1):##Case where we have wrapped around and there is more than one element to the right of back
            last_elm =self.data_[self.back_]#Store last element before we remove it 
            self.data_.remove(self.data_[self.back_])
            self.front_ =-1
            self.back_  =-1
            self.size_  -=1
            return last_elm
        elif(self.back_==-1 and self.size_==1):##Case where we have already wrapped around now there is exactly one element left at back and now we need to reverse wrap and put back at the 0th index
            last_elm =self.data_[self.back_]#Store last element before we remove it 
            self.data_.remove(self.data_[self.back_])
            self.front_ =-1
            self.back_  =0
            self.size_  -=1
            return last_elm
        else:#The Back is not at the first index(possibly somewhere in between) and if we pop it we have to go down by one for the new back
           last_elm = self.data_[self.back_]#Normal pop
           self.data_.remove(self.data_[self.back_])
           self.back_-=1
           self.size_-=1
           return last_elm
       

    def clear(self):
        """
        Removes all elements from the Deque
        :return:
        """
        self.data_.clear()#Beauty of array implementation, we call .clear() and wipe our Deque 
        self.size_=0#Deque should now be empty

    def retain_if(self, condition):
        """
        Removes items from the Deque so that only items satisfying the given condition remain
        :param condition: A boolean function that tests elements
        """
        for item in(self.data_):
            if(item !=None):#Ignore space that we haven't filled yet
                if not condition(item):
                    self.data_.remove(item)
                    self.size_-=1

    def __iter__(self):
        """
        Iterates over this Deque from front to back
        :return: An iterator
        """
        for item in(self.data_):
            if(item!= None):#We dont want to yield spaces that have not been filled yet 
                yield item
        
    # provided functions

    def is_empty(self):
        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this Deque
        :return: A string
        """
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))

