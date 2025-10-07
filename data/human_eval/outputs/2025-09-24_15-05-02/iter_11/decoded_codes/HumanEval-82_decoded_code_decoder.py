def prime_length(string):
    length = len(string)
    if length == 0 or length == 1:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True