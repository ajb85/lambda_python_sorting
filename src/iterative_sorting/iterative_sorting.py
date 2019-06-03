# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

arr = [5,4,3,3,2,6,7,1,17]

print(selection_sort(arr))