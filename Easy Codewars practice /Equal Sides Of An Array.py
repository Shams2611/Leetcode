def find_even_index(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1:])
        
        if left_sum == right_sum:
            return i
        
    return -1


#More efficient method 

def find_even_index(array):
    #your code here
	for k,v in enumerate(array): 
		if (sum(array[0:k]) == sum(array[k+1:])): return k
	return -1