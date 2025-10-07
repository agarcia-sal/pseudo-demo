def sort_third(l: list) -> list:
    l = list(l)
    indices_divisible_by_three = []
    elements_at_divisible_indices = []
    length_of_l = len(l)

    for index in range(length_of_l):
        if index % 3 == 0:
            indices_divisible_by_three.append(index)
            elements_at_divisible_indices.append(l[index])

    elements_at_divisible_indices.sort()

    for i in range(len(indices_divisible_by_three)):
        index = indices_divisible_by_three[i]
        l[index] = elements_at_divisible_by_three[i]

    return l