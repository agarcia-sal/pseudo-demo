def fruit_distribution(s, n):
    lis = []
    for word in s.split():
        if word.isdigit():
            lis.append(int(word))
    return n - sum(lis)