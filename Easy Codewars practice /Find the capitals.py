def capitals(word):
    new_list = []
    
    for i in range(len(word)):
        if word[i].isupper():
            new_list.append(i)
    return new_list

#using lambda 

def capitals(word):
    return filter(lambda x: word[x].isupper(), range(len(word)))