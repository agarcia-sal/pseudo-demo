def sort_third(l: list):
    l = list(l)
    indices_divisible_by_three = [i for i in range(len(l)) if i % 3 == 0]
    values_at_divisible_indices = [l[i] for i in indices_divisible_by_three]
    sorted_values = sorted(values_at_divisible_indices)
    for pos, index in enumerate(indices_divisible_by_three):
        l[index] = sorted_values[pos]
    return l