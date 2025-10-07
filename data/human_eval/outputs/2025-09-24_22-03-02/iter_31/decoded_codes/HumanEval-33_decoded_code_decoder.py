def sort_third(l: list):
    l = list(l)
    indices_divisible_by_three = []
    values_at_divisible_indices = []
    length_of_l = len(l)
    for index in range(length_of_l):
        if index % 3 == 0:
            indices_divisible_by_three.append(index)
            values_at_divisible_indices.append(l[index])
    sorted_values = sorted(values_at_divisible_indices)
    for counter, index_to_replace in enumerate(indices_divisible_by_three):
        l[index_to_replace] = sorted_values[counter]
    return l