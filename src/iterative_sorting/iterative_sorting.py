# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # O(n)
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap

        # After first iteration, smallest should be on left side of the list.
        # So we can start counting from wherever 'i' is (and thus compare to i+1)
        for j in range(i+1, len(arr)): #
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # The highest number will always end up at the end after each iteration through the list  
    # Thus, after each iteration I can check one fewer index.  Easiest way to do this is
    # Have one loop count at the end, down to the front while the other loop counts from 0
    # to the parent loop's counter variable
    for i in range(len(arr)-1,0,-1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

arr = [5,4,3,1,17]
