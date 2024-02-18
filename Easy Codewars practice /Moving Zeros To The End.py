#first wrong attempt 

def move_zeros(lst):
    count = 0
    for i in lst:
        if list[i] == 0:
            list.pop(i)
            count += 1
    zeroes = [0] * count
    
    return lst + zeroes


#correct method 

def move_zeros(lst):
    non_zeroes = [x for x in lst if x!= 0]
    zeroes = [0] * (len(lst) - len(non_zeroes))
    
    lst[:] = non_zeroes + zeroes 
    
    return lsts

#very similar to my first attempt

def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array