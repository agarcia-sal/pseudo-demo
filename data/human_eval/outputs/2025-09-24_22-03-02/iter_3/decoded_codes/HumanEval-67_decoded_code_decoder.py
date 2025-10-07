def fruit_distribution(s, n):
    return n - sum(int(i) for i in s.split() if i.isdigit())