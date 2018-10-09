import copy,math
import numpy as np

""""
#Sources 
https://codereview.stackexchange.com/questions/147346/hash-table-using-linear-probing
https://codereview.stackexchange.com/questions/118110/python-hash-table-implementation
https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-an-array-in-python
"""

class HashMap:
    def __init__(self, load_factor=1.00,capacity= 10):
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
        """
        We loop through are hash map with a start point and a copy of it. We continuously refresh the start copy
        until we cycle back to the orgianl start's position. If this happens we didn't find the key. Else
        we did find it and return true verify its in our hashmap
        
        """
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
    def find(self,key):
        """
        We apply the same logic that we used in our get function with a slight difference. We are looking
        for the actaul slot index value of the target key instead of the keys value
        """
    	# Returns value types
        startslot = self.hashfunction(key)
        key_index = 0
        position = startslot
        while self.hashkey[position] !=startslot:
            if self.hashkey[position] == key:
                key_index = position
                break
            else:
                position=self.rehash(position)
                if position == startslot:
                    break
        return key_index        

    def get(self,key):
        """
        Set a start point and a copy of it to be updated and a target value set to none. As we update the start copy
        if we loop through the entire Hashmap and don't find the value of they key we return a target value 
        of None and raise a KeyError. Else we return the data
        """
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
            raise KeyError
        return data        

    def put(self,key,value):
        hashvalue = self.hashfunction(key)
        nextslot = hashvalue
        #If we enter this block we will just add normally
        if self.hashkey[hashvalue] is None:
            self.hashkey[hashvalue] = key
            self.values[hashvalue] = value
            self.size+=1
            self.checkGrow()
        elif key in self:
            """
            To prevent the instance where we update the wrong key's value beacuse its slot is drawn up again by rehash
            we use the helper find  function to locate the orginal slot for the key we want to update
            then we apply the update. 
            """
            key_index = self.find(key)#Update the original keys value
            self.values[key_index] = value
#            print("hashvalue slot",hashvalue," ","new slot"," ",nextslot)
#            print("hashvalue slot"," ",hashvalue," ","new value"," ",value," ","original key"," ",key," ","new key to be inserted?"," ",self.hashkey[nextslot])
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
            else: 
#                key_slot = self.find(key)
#                self.hashkey[key_slot] = value
                return 
    def delete(self,key):
        """
        We loop through are hash map with a start point and a copy of it. We continuously refresh the start copy
        until we cycle back to the orgianl start's position. If this happens we didn't find the key we want to
         to remove Else we did find it and we remove it and record its deletion
        """
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
       key_set = set()#Init key set
       for key in self.hashkey:
           if key!=None:#Add keys from hashkey set excluding the weird instance of none
               key_set.add(key)
#       print(key_set)
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
    """
    We init a new hashmap to store our unique words with the amount of times they appear in the seq as their values.
    We iterate through the sequencce of words and if they arent already in our hashmap we insert them with
    the amount of times they appear in the seq of text as their vaule.
    """
    word_hash = HashMap()#Initialize a hashmap to store our unique words mapped to their freq
#    print(word_hash.hashkey)
    count = 0
    for word in seq:#iterate through text
        if word not in word_hash:
            word_hash[word]=count+1#
        elif word in word_hash:
            word_hash[word]+=1
    return word_hash
  
