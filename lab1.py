#function to use iteration to determine the largest integer value in a given list of integers
def max_list_iter(int_list):

    #if the list is None, raises value error
    if(int_list == None):
        raise ValueError
    
    #sets integer 'largest' as the value of the first item in the list
    largest = int_list[0]
    
    #for loop for running through every item in the list
    for i in range(len(int_list)):
    
        #if value of current list item is larger than current largest...
        if(int_list[i] > largest):
            #...'largest' is reassigned to this value
            largest = int_list[i]

    return(largest)
    
    pass

#recursive function to reverse the contents of a list
def reverse_rec(int_list):
    
    #if the list is None, raises ValueError
    if(int_list==None):
        raise ValueError
    
    #returns empty list at final recursion
    if(len(int_list)==0):
        return []
    
    #recursive, calling function with shrinking list and adding first element of int_list at each recursion
    return (reverse_rec(int_list[1:])) + int_list[0:1]

    pass

#recursive function to return index of target number in a list
def bin_search(target, low, high, int_list):

    #if list is none, ValueError
    if(int_list == None):
        raise ValueError
    
    #for edge cases where infinite recursion caused by lists with short lengths
    if(len(int_list) == 1):
        return 0
    elif(low == int((low+high)/2)):
        middle_index = low + 1
    elif (high == int((low+high)/2)):
        middle_index = high - 1
    else:
        middle_index = int(low+high)//2
    
    #if target is not in list, return None
    if(target not in int_list):
        return None
    
    #for edge case where length = 1
    elif(middle_index < 0):
        return middle_index + 1
        
    #return current middle_index of its value is target
    elif(int_list[middle_index] == target):
        return middle_index
    
    #recursive, replacing high with middle_index
    elif(int_list[middle_index] > target):
        return bin_search(target, low, middle_index, int_list)
        
    #recursive, replcaing low with middle_index
    elif(int_list[middle_index] < target):
        return bin_search(target, middle_index, high, int_list)

    pass
