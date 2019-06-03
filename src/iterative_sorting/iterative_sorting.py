# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # O(n)
        cur_index = i
        smallest_index = cur_index

        # After first iteration, smallest should be on left side of the list.
        # So we can start counting from wherever 'i' is (and thus compare to i+1)
        for j in range(i+1, len(arr)): # O(n)
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr # --> O(n^2)

def bubble_sort( arr ):
    # The highest number will always end up at the end after each iteration through the list  
    # Thus, after each iteration I can check one fewer index.  Easiest way to do this is
    # Have one loop count at the end, down to the front while the other loop counts from 0
    # to the parent loop's counter variable
    for i in range(len(arr)-1,0,-1): # O(n)
        for j in range(0, i): # O(n)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr # O(n^2)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if(not len(arr)):
        return []
    maxValue = max(*arr) if maximum == -1 else maximum
    if(min(*arr) < 0):
        return "Error, negative numbers not allowed in Count Sort"
    count = [0 for x in range(maxValue+1)] # O(m)

    for i in range(len(arr)): # O(n)
        num = arr[i]
        count[num] += 1

    answer = []

    # This works but it feels really sloppy.  Is there an easy way to insert Y duplicates of X into a list?
    for i in range(len(count)): # O(m)
        if(count[i]>0):
            for j in range(count[i]): # O(n)
                answer.append(i)

    return answer # 2*O(n) + 2*O(m) --> 2*O(n+m) --> O(n+m)



arr = [5,4,3,1,17,1,2,1,3]

print(count_sort(arr))
