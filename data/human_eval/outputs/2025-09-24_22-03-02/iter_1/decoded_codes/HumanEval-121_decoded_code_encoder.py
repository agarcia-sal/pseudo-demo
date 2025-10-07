def sum_odd_in_even_pos(lst):
    sum_odd_in_even_pos = sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)
    return sum_odd_in_even_pos