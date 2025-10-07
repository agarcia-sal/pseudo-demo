def prime_length(input_string):
    length = len(input_string)
    if length == 0 or length == 1:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True