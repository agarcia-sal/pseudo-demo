def sort_third(l: list) -> list:
    l = list(l)
    indices_divisible_by_three = []
    values_at_divisible_indices = []
    index = 0
    while index < len(l):
        if index % 3 == 0:
            indices_divisible_by_three.append(index)
            values_at_divisible_indices.append(l[index])
        index += 1
    sorted_values = sorted(values_at_divisible_indices)
    i = 0
    while i < len(indices_divisible_by_three):
        index_to_replace = indices_divisible_by_three[i]
        l[index_to_replace] = sorted_values[i]
        i += 1
    return l