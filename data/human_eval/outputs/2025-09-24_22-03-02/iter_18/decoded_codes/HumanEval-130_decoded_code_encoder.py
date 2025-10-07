def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(1 + i // 2)
        else:
            left_value = my_tri[i - 1]
            middle_value = my_tri[i - 2]
            right_value = 3 + i // 2
            my_tri.append(left_value + middle_value + right_value)
    return my_tri