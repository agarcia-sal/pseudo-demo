def checkConsecutiveNumbers(n):
    is_true = [True] * n
    j = 0
    i = 1

    while i <= 500000:
        if is_true[j]:
            is_true[j] = False  # Mark the current position as False
        i += 1
        j = (j + i) % n  # Move to the next index based on the current step

    remaining_true = [value for value in is_true if value]

    if len(remaining_true) == 0:
        print('YES')  # All positions have been marked False
    else:
        print('NO')   # There are still True values indicating some positions are unmarked
