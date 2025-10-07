def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            value = 1 + i // 2
            my_tri.append(value)
        else:
            term1 = my_tri[i - 1]
            term2 = my_tri[i - 2]
            term3 = (i + 3) // 2
            value = term1 + term2 + term3
            my_tri.append(value)
    return my_tri