def sort_third(l: list) -> list:
    l_copy = l[:]
    divisible_indices_values = [l_copy[i] for i in range(len(l_copy)) if i % 3 == 0]
    sorted_divisible_indices_values = sorted(divisible_indices_values)
    sorted_index = 0
    for i in range(len(l_copy)):
        if i % 3 == 0:
            l_copy[i] = sorted_divisible_indices_values[sorted_index]
            sorted_index += 1
    return l_copy