def solution(s):
    result = ""
    for char in s:
        if char.isupper():
            result += " "
        result += char
            
    return result

#One liner 

def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)