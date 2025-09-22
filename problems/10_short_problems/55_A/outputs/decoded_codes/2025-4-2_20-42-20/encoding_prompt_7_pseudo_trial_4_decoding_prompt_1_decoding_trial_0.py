def checkConsecutiveNumbers(n):
    is_true = [True] * n  # Initialize an array 'is_true' of size n with all values set to True
    j = 0  # Initialize index 'j' to 0
    i = 1  # Initialize step 'i' to 1

    while i <= 500000:  # WHILE step 'i' is less than or equal to 500000 DO
        if is_true[j]:  # IF 'is_true[j]' is True THEN
            is_true[j] = False  # Mark the current position as False
        i += 1  # INCREMENT step 'i' by 1
        j = (j + i) % n  # UPDATE index 'j'

    remaining_true = [value for value in is_true if value]  # Initialize list 'remaining_true'

    if len(remaining_true) == 0:  # IF the length of 'remaining_true' is equal to 0 THEN
        print('YES')  # All positions have been marked False
    else:
        print('NO')  # There are still True values indicating some positions are unmarked
