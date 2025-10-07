def add(lst) -> int:
    sum_even_at_odd_indices = 0
    for index in range(1, len(lst), 2):
        if lst[index] % 2 == 0:
            sum_even_at_odd_indices += lst[index]
    return sum_even_at_odd_indices