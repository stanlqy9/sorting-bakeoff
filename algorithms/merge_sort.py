def merge_sort(a_list):
    # Using the classic top-down recusrive divide and conquer
    # split -> recurse left -> recurse right -> merge

    # 'a_list' is the array list of intergers accepted in the argument
    # Program returns the sorted array list and the total comparison count

    array = a_list[:]
    comparisons = [0]

    def merge_inner_sort(array, start_point, end_point):
        if end_point - start_point > 1:
            middle = (start_point + end_point) // 2
            merge_inner_sort(array, start_point, middle)
            merge_inner_sort(array, middle, end_point)
            merge(array, start_point, middle, end_point)

        else:
            return

    def merge(array, start_point, middle, end_point):
        start_point_half_array = array[start_point:middle]
        right_half_array = array[middle:end_point]
        i = 0 
        j = 0
        k = start_point

        while i < len(start_point_half_array) and j < len(right_half_array):
            comparisons[0] += 1

            if start_point_half_array[i] <= right_half_array[j]:
                array[k] = start_point_half_array[i]
                i += 1

            else:
                array[k] = right_half_array[j]
                j += 1

            k += 1

        if i == len(start_point_half_array):
            while j < len(right_half_array):
                array[k] = right_half_array[j]
                j += 1
                k += 1
        
        else:
            while i < len(start_point_half_array):
                array[k] = start_point_half_array[i]
                i += 1
                k += 1
    
    merge_inner_sort(array, 0, len(array))
    return array, comparisons[0]
