def capitals(word):
    new_list = []
    
    for i in range(len(word)):
        if word[i].isupper():
            new_list.append(i)
    return new_list
        