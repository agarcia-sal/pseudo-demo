def largest_divisor(integer_n: int) -> int:
    counter = integer_n - 1
    while counter > 0:
        if integer_n % counter == 0:
            return counter
        counter -= 1
    # integer_n > 0 always ensures the while loop returns before this; 
    # but for completeness if integer_n <= 1:
    return 0