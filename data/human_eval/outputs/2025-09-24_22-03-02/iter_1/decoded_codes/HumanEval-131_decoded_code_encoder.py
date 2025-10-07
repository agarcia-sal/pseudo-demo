def digits(n):
    product = 1
    odd_count = 0
    for d in str(n):
        if int(d) % 2 == 1:
            product *= int(d)
            odd_count += 1
    return 0 if odd_count == 0 else product