def fruit_distribution(s, n):
    lis = []
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)