#insertion sort draft-up
def insertion_sort(input_list):
    arr = input_list.copy() # copy, so the original list is not changed
    comparisons = 0 # count how many comparisons we make 
    swaps = 0 # count shifts/assignemnts

   #starting from the second element since the first is already "sorted"
    for i in range(1, len(input_list)):
        anchor = arr[i] # the current value we want to insert into the sorted part 
        j = i - 1 # start checking from the element just before anchor

       # moving left while elemnts are bigger than anchor
        while j >= 0:  
          comparisons += 1 # coun this comparison 

          if  anchor < arr[j]:  # shift bigger element one spot to the right 
              arr[j+1] = arr[j] 
              swaps +=1  # move left to keep checking
              j-= 1
        else:
              break   # stop when the correct position is found
        
    #place anchor into its correct sorted position     
    if j + 1 != i:
        arr[j+1] = anchor
        swaps += 1

        # return the sorted list and its counts
        return arr, comparisons, swaps