def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i // 2 + 1)
        else:
            value1 = my_tri[i - 1]
            value2 = my_tri[i - 2]
            value3 = (i + 3) // 2
            my_tri.append(value1 + value2 + value3)
    return my_tri