import copy,math
import numpy as np
from itertools import groupby

class HashMap:
    def __init__(self, load_factor=1.00, capacity= 4):
        # You may change the default maximum load factor
        self.max_load_factor = load_factor
        # Other initialization code can go here
        self.min_capacity = capacity
        self.capacity = capacity
        self.size = 0
        self.hashkey= [None]*self.capacity
        self.values= [None]*self.capacity
        
        

    def hashfunction(self,key):
        return hash(key) % self.capacity

    def rehash(self,oldhash):
        return (oldhash+1)%self.capacity
    
    def __len__(self):
#        count = 0
#        for key, value in zip(self.hashkey,self.values):
#                if key and value !=None:
#                    count+=1
        return self.size
    def checkGrow(self):
        if self.size >= self.capacity:
                self.grow()
    def checkShrink(self):
      if self.size < self.max_load_factor*0.25 *self.capacity and self.capacity >= self.min_capacity* 2:
            self.shrink()


        
    def load(self):
        return self.size/math.floor((self.capacity))
    
    def grow(self):
        new_capacity= 2*self.capacity
        new_hashmap = HashMap(1.00,new_capacity)
#        print("new map", new_hashmap, "new hashkeys", new_hashmap.hashkey)
        for key in self.hashkey:
            if key != None:
                new_hashmap.put(key, self.get(key))
#                print("new hash", new_hashmap)
        self.capacity = new_capacity
        self.hashkey = copy.copy(new_hashmap.hashkey)
        self.values = copy.copy(new_hashmap.values)
#        print(self.hashkey)
#        print("new hash", new_hashmap)
#        del new_hashmap
    def shrink(self):
        new_capacity=self.capacity//2
        new_hashmap = HashMap(1.00,new_capacity)
#        print("new map", new_hashmap, "new hashkeys", new_hashmap.hashkey)
        for key in self.hashkey:
            if key != None:
                new_hashmap.put(key, self.get(key))
#                print("new hash", new_hashmap)
        self.capacity = new_capacity
        self.hashkey = copy.copy(new_hashmap.hashkey)
        self.values = copy.copy(new_hashmap.values)
#        print(self.hashkey)
#        print("new hash", new_hashmap)
#        del new_hashmap




    def __contains__(self, key):
        startslot = self.hashfunction(key)
        stop = False
        found = False
        position = startslot
        while self.hashkey[position] != startslot and not found and not stop:
            if self.hashkey[position] == key:
                found = True
            else:
                position=self.rehash(position)
#                print("pos",position, "startslot", startslot)
                if position == startslot:
#                    print("do we enter this")
                    stop = True
#        print("do we get here")
        return found       

    def get(self,key):
    	# Returns value types
        startslot = self.hashfunction(key)
        data = None
        position = startslot
        while self.hashkey[position] !=startslot:
            if self.hashkey[position] == key:
                data = self.values[position]
                break
            else:
                position=self.rehash(position)
                if position == startslot:
                    break
        if data == None: 
            raise KeyError(key)
        return data        

    def put(self,key,value):
        hashvalue = self.hashfunction(key)
        nextslot = hashvalue
        #If we enter this block we will just add normally
#        if self.size >= self.capacity:
#            print("do we get here")
#            print(self.hashkey)
#            self.resize()
        if self.hashkey[hashvalue] is None:
            self.hashkey[hashvalue] = key
            self.values[hashvalue] = value
            self.size+=1
#            print("here3")
            self.checkGrow()
            #If we trigger this block we need to grow our hash table
#            print("size",self.size)
        elif key in self:
            print("hashvalue slot",hashvalue," ","new slot"," ",nextslot)
            self.values[nextslot] = value
            print("hashvalue slot"," ",hashvalue," ","new value"," ",value," ","key"," ",self.hashkey[nextslot])
              

        else:
            nextslot = self.rehash(hashvalue)
            # Loop until you find an empty slot.
            while (self.hashkey[nextslot]!=None) and (nextslot != hashvalue) and self.hashkey[hashvalue] != key:      
                nextslot = self.rehash(nextslot)
                # Double check if we found an empty spot
            if self.hashkey[nextslot] is None: 
                self.hashkey[nextslot] = key
                self.values[nextslot] = value
                self.size+=1
                self.checkGrow()
#                print("here1")
                return
            elif key not in self:
#                print("hello")
                if self.hashkey[nextslot]is None:
                    nextslot = self.rehash(nextslot)
                    self.hashkey[nextslot] = value
#                print("here2")

                self.values[hashvalue] = value
#               print("size",self.size)
#               elif self.size >= self.capacity:// "Will be used later"
#                    print("do we get here")
#                    self.resize()
#                    self.put(key,value)       
                        
            else: 
                self.values[hashvalue] = value
                return 
    def delete(self,key):
        initial_val = self.hashfunction(key)#Set a starting point to prevent inf looping
#        print("ini val", initial_val)
        hashvalue = initial_val
        return_value = None
#        loop_count =0
        while (self.hashkey[hashvalue]!=initial_val):#Loop through table until we get back to where we started 
#            loop_count+=1// Bug checking
#            print("loop count", loop_count)// Bug checking
            if self.hashkey[hashvalue] == key:
                return_value = self.values[hashvalue]#We find the key we want to delete and record it
                self.hashkey[hashvalue] = None
                self.values[hashvalue] = None
                self.size-=1
                self.checkShrink()
                break
            else:
                hashvalue = self.rehash(hashvalue)
#                print("hashvalue", hashvalue)
                if hashvalue == initial_val:
                    break 
        if return_value == None:#If we exit the while loop and the the return value is still none than we didnt find it
            raise KeyError     # Thus, we show raise an error
        return
                    
        
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        return self.put(key,value)

    def __delitem__(self, key):
        return self.delete(key)

    def __iter__(self):
        for key, value in zip(self.hashkey,self.values):
            if key and value !=None:
                yield key,value
               
    def clear(self):
        self.hashkey= [None]*self.capacity
        self.values = [None]*self.capacity
        self.size=0
        self.capacity = self.capacity

    def keys(self):
       key_set = set()
       for key in self.hashkey:
           if key!=None:
               key_set.add(key)
       print(key_set)
       return key_set

    # supplied methods

    def __repr__(self):
        return '{{{0}}}'.format(', '.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):
        return not self.is_empty()

    def is_empty(self):
        return len(self) == 0

    # Helper functions can go here
    


# Required Function
def word_frequency(seq):
    word_hash = HashMap()
    print(word_hash.hashkey)
    word_count =[]
    for word in seq:
            word_count.append(word)
    print(word_count)
#    word_freq = [len(list(group)) for key, group in groupby(word_count)]
#    print(word_freq)
    unique_elements, counts_elements = np.unique(word_count, return_counts=True)
#    print(counts_elements)
    for word_unique,word_freq in zip(unique_elements,counts_elements):
          word_hash.put(word_unique,word_freq)
    print(len(word_hash.hashkey))
    print(word_hash.size)
    return word_hash
