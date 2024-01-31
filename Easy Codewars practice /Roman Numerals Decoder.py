def solution(roman : str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    total = 0
    previous = 0
    
    for char in reversed(roman):
        current_value = roman_values[char]
        
        if current_value < previous:
            total -= current_value
        else:
            total += current_value
            
        previous = current_value
            
    return total
    