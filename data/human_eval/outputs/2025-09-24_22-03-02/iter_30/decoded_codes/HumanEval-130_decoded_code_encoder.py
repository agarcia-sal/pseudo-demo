def tri(n):
    if n == 0:
        return [1]

    my_tri = [1, 3]

    for i in range(2, n):
        if i % 2 == 0:
            value = 1 + i // 2
            my_tri.append(value)
        else:
            left = my_tri[i - 1]
            middle = my_tri[i - 2]
            right = 3 + i // 2
            value = left + middle + right
            my_tri.append(value)

    return my_tri