#My bad attempt 

def scramble(s1, s2):
    hashmap1 = {}
    hashmap2 = {}
    
    pair1 = s1.split('')
    pair2 = s2.split('')
    
    for pair in pair1:
        key, value = pair1.split('=')
        hashmap1[key] = value
        
    for pair in pair2:
        key, value = pair2.split('=')
        hashmap2[key] = value
        
        
    if hashmap1 == hashmap2:
        return True
    else:
        return False


#Creative way to do it


def scramble(s1, s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
        
    return True