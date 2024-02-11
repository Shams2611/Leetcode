def rot13(message):
    new_message = ""
    for char in message:
        if 'a' <= char <= 'z':
            new_message += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            new_message += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            new_message += char
        
    return new_message

#Creative but stupid way to do it 

def rot13(message):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cba = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    mytable = message.maketrans(abc, cba)
    return message.translate(mytable)