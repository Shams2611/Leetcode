def first_non_repeating_letter(s):
    # Iterate through each character in the string
    for char in s:
        # Check if the lowercase version of the character occurs only once
        if s.lower().count(char.lower()) == 1:
            return char
    # If no non-repeating character is found, return an empty string
    return ""
