my_array = [64, 34, 25, 5, 22, 11, 90, 12];

array_length = len(my_array);

for i in range(array_length-1):
    
    #Init the min index
    min_index = i;
     
    for j in range(i+1, array_length):
        #Check the diff in size
        if my_array[j] < my_array[min_index]:
            min_index = j;
            
    my_array[i],my_array[min_index] = my_array[min_index],my_array[i];
    
print(my_array)

