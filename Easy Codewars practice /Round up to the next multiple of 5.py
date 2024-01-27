def round_to_next5(n):
    remainder = n % 5
    if remainder == 0:
        return n
    else:
        return n + (5 - remainder)