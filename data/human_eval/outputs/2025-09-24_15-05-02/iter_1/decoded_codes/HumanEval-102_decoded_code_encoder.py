def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0 and y >= x:
        return y
    if y - 1 >= x and (y - 1) % 2 == 0:
        return y - 1
    return -1