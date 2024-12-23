my_array = [3, 7, 6, -10, 15, 23.5, 55, -13]

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

print(binarySearch(my_array, 55))
        
        