def sum_squares(lst):
    import math
    squared = 0
    for index in range(len(lst)):
        i = lst[index]
        ceil_i = math.ceil(i)
        square_ceil_i = ceil_i * ceil_i
        squared += square_ceil_i
    return squared