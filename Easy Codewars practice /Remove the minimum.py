def remove_smallest(numbers):
    if not numbers:
        return []
    min_number = min(numbers)
    min_index = numbers.index(min_number)
    
    return numbers[:min_index] + numbers[min_index + 1:]
