def rounded_avg(n, m):
    # Return -1 if m is less than n
    if m < n:
        return -1

    # Calculate the sum from n to m inclusive using arithmetic series formula for efficiency
    count = m - n + 1
    summation = (n + m) * count // 2

    # Calculate the average and round it
    average = summation / count
    rounded_average = round(average)

    # Convert the rounded average to binary string without the '0b' prefix
    binary_result = bin(rounded_average)[2:]

    return binary_result