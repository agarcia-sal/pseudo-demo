n = abs(int(input()))
i = 0

while True:
    s = i * (i + 1) // 2  # Sum of the first i integers
    m = s - n             # Difference between sum and n

    if s == n:
        print(i)
        break
    elif s > n:
        if m % 2 == 0:    # Check if the difference is even
            print(i)
            break

    i += 1
