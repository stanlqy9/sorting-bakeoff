#Selection sort draft up 

def selection_sort(input_list):
    arr = input_list.copy() # copy, so the original list is not changed
    comparisons = 0 # count how many comparisons we make 
    swaps = 0 # count shifts/assignemnts

    n = len(arr)
    #move through each position in the list 
    for i in range(n):
        min_index = i # assume current position has smallest value
    
    #look at the smallest value in the rest of the list
    for j in range (i +1, n):
        comparisons += 1
        
        if arr[j] < arr[min_index]:
            min_index = j 
        
        #swap only if we found the smallest value
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

#return sorted list & counts
    return arr, comparisons, swaps
    

