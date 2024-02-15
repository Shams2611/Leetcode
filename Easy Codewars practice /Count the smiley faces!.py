def count_smileys(arr):
    count = 0
    
    valid_eye = {':', ';'}
    valid_nose = {'-', '~'}
    valid_smile = {')', 'D'}
    
    
    for emoji in arr:
        if len(emoji) == 2:
            if emoji[0] in valid_eye and emoji[1] in valid_smile:
                count += 1
                
        elif len(emoji) == 3:
            if emoji[0] in valid_eye and emoji[1] in valid_nose and emoji[2] in valid_smile:
                count += 1
        else:
            return 0
        
    return count
            