my_array = [7,8,3,4,9,10];
array_length = len(my_array);

for i in range(array_length - 1):
    swapped = False;
    for j in  range(array_length - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j];
            swapped = True
    if not swapped:
        break;
    
print(my_array)


