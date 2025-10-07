def digits(n):
    product = 1
    odd_count = 0
    for d in str(n):
        i = int(d)
        if i % 2 == 1:
            product *= i
            odd_count += 1
    return product if odd_count else 0