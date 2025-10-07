def sum_squares(lst):
    import math
    squared = 0
    for i in lst:
        ceil_i = math.ceil(i)
        squared += ceil_i * ceil_i
    return squared