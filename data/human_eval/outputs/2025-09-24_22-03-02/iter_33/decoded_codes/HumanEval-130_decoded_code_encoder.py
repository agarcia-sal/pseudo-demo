def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    i = 2
    while i <= n:
        if i % 2 == 0:
            value = 1 + i // 2
            my_tri.append(value)
        else:
            value = my_tri[i - 1] + my_tri[i - 2] + (i + 3) // 2
            my_tri.append(value)
        i += 1
    return my_tri