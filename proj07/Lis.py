"""
Sources
https://stackoverflow.com/questions/3992697/longest-increasing-subsequence?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
https://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""

def verify_subseq(seq, subseq):
    """
    iterate through the subseq and check to see if
    it exists in the actual seq. We keep track of every instance we find 
    a matching "char" of the subseq in the seq
    """
    if len(seq)==0 or len(subseq) == 0:
        return True
    length =(len(subseq))
    verify_count =0
    for i in range(0,len(subseq)):
        if subseq[i] in seq:
            verify_count+=1
    if verify_count == length:#If verify count matches the length of the subseq then we know each element 
            return True#in the subseq matched to an element in the actual "seq"
    else:
        return False 

def verify_increasing(seq):
    """
    iterate through the seqand check to see if
    previous element is less than current.
    If this condition does not hold we return false
    """
    if len(seq)==0:
        return True
    previous = 0
    result = True
    for index in range(1,len(seq)):
        current = index
        if seq[previous] >= seq[current]:
            result = False 
            return result
        else:
            previous = current
    return result
            
def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for i in range(L):
        result.append(seq[pos])
        pos = P[pos]
    result.reverse()
    return result  # reversing  


def find_lis(seq):
    return subsequence(seq)
