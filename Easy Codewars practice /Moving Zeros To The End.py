#first wrong attempt 

def move_zeros(lst):
    count = 0
    for i in lst:
        if list[i] == 0:
            list.pop(i)
            count += 1
    zeroes = [0] * count
    
    return lst + zeroes