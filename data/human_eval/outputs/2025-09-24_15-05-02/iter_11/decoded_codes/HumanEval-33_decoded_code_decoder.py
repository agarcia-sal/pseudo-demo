def sort_third(list_l):
    list_l = list(list_l)
    elements_at_indices_divisible_by_three = [list_l[i] for i in range(len(list_l)) if i % 3 == 0]
    sorted_elements = sorted(elements_at_indices_divisible_by_three)
    idx = 0
    for i in range(len(list_l)):
        if i % 3 == 0:
            list_l[i] = sorted_elements[idx]
            idx += 1
    return list_l