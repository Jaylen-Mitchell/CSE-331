	
def order_first_name(a, b):
    """
	Orders two people by their first names
	:param a: a Person
	:param b: a Person
	:return: True if a comes before b alphabetically and False otherwise
	"""
    if (a.first < b.first):
        return True
    elif (a.first==b.first):
        return a.last < b.last# Return value will be true if person's A last name comes before person B and false otherwise
    else: 
        return False#If we trigger this then person A > B 
   
def order_last_name(a, b):
    """
	Orders two people by their first names
	:param a: a Person
	:param b: a Person
	:return: True if a comes before b alphabetically and False otherwise
    """
    if (a.last < b.last):
        return True
    elif (a.last==b.last):#If we got here then person a and person b had the same first name thus, we should compare their last names
        return a.first < b.first# Return value will be true if person's A first name comes before person B and false otherwise
    else:
        return False #If we trigger this then person A > B 



def is_alphabetized(roster, ordering):
    """
	Checks whether the roster of names is alphabetized in the given order
	:param roster: a list of people
	:param ordering: a function comparing two elements
	:return: True if the roster is alphabetized and False otherwise
	"""
    for i in range(1,len(roster),1):
        current_person = i
        previous_person= i-1
        if not ordering(roster[previous_person],roster[current_person]):
            return False
    return True

#Source https://stackoverflow.com/questions/10502533/explanation-of-merge-sort-for-dummies
def merge(ordering, left, right, comparison_count):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if (ordering(left[i],right[j])):#We will sort the people within the two list by using our odering comparision
            result.append(left[i])#If the comparions checks out that person a in first list aka left  comes before person b in the second list aka right
            i += 1                #We will then add them to the master list.
            comparison_count+=1
        else:
            result.append(right[j])#If we got here our person b in the second list should have come before a in the first list :( but thats okay!
            j += 1                  #We will amend this by adding person to the master result list which is built up to maintain a sorted order
            comparison_count+=1
    result += left[i:]
    result += right[j:]
    return result,comparison_count
#Source: https://stackoverflow.com/questions/10502533/explanation-of-merge-sort-for-dummies
def mergesort(list, ordering):#
    comparison_count=0
    if len(list) < 2:#If length reaches a length smaller than two we don't need to make a comparison since there would onyl be one element  
        return list,0
    middle = len(list) // 2#Split list into two halves
    left,l_count = mergesort(list[:middle],ordering)#Left half will be everything up to the middle pt
    comparison_count+= l_count#Eveytime we split up the two halfs further breaking them down until the length of the sublists(left,right) is smaller than 2 we count the compairsons we make
    right,r_count = mergesort(list[middle:],ordering)#Right half will be everything after the middle pt 
    comparison_count+=r_count
    return merge(ordering, left, right,comparison_count)
	
def alphabetize(roster, ordering):
    """
	Alphabetizes the roster according to the given ordering
	:param roster: a list of people
	:param ordering: a function comparing two elements
	:return: a sorted version of roster
	:return: the number of comparisons made
	"""
#    if len(roster) < 2:
#        return list
#    middle = len(roster) // 2#Split list into two halves
#    left = (roster[:middle])#Left half will be everything up to the middle pt
#    print("left half",left)
#    right =(roster[middle:])#Right half will be everything after the middle pt 
#    print("right half",right)
#    
#    result = []
#    comparison=0
#    i ,j = 0, 0
#    while i < len(left) and j < len(right):
#        if ordering(left[i],right[j]):#We will sort the people within the two list by using our odering comparision
#            print(ordering(left[i],right[j]))
#            result.append(left[i])#If the comparions checks out that person a in first list aka left  comes before person b in the second list aka right
#            i += 1                #We will then add them to the master list.
#            comparison+=1
#        else:
#            result.append(right[j])#If we got here our person b in the second list should have come before a in the first list :( but thats okay!
#            j += 1                  #We will amend this by adding person to the master result list which is built up to maintain a sorted order
#            comparison+=1
#    result += left[i:]
#    result += right[j:]
#   # print(result)
#    print(comparison)
    result = mergesort(roster,ordering,)
    final_result = result[0]
    final_comparison_count= result[1]
    return (final_result,final_comparison_count)

