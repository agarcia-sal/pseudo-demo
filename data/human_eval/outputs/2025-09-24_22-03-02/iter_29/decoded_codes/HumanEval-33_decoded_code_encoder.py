def sort_third(l: list) -> list:
    l = list(l)
    indices_divisible_by_three = []
    values_at_divisible_indices = []
    length_l = len(l)
    for i in range(length_l):
        if i % 3 == 0:
            indices_divisible_by_three.append(i)
            values_at_divisible_indices.append(l[i])
    sorted_values = sorted(values_at_divisible_indices)
    for j in range(len(indices_divisible_by_three)):
        index_to_replace = indices_divisible_by_three[j]
        l[index_to_replace] = sorted_values[j]
    return l