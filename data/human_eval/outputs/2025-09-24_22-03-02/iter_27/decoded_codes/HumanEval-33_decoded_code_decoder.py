def sort_third(l: list):
    l = list(l)
    indices_divisible_by_three = []
    values_at_indices = []
    for i in range(len(l)):
        if i % 3 == 0:
            indices_divisible_by_three.append(i)
            values_at_indices.append(l[i])
    sorted_values = sorted(values_at_indices)
    for j in range(len(indices_divisible_by_three)):
        index = indices_divisible_by_three[j]
        l[index] = sorted_values[j]
    return l