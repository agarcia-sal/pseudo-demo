def unique_digits(x):
    return sorted([i for i in x if all(int(d) % 2 == 1 for d in str(i))])