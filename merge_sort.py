my_array = [3, 7, 6, -10, 15, 23.5, 55, -13];

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    leftHalf = arr[:mid]
    rigthHalf = arr[mid:]
    
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rigthHalf)
    
    return merge(sortedLeft, sortedRight)



def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

print(mergeSort(my_array))
    