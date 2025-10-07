def sort_third(l: list) -> list:
    l = l.copy()
    elements_at_indices_divisible_by_three = [l[i] for i in range(0, len(l), 3)]
    sorted_elements = sorted(elements_at_indices_divisible_by_three)
    for idx, val in zip(range(0, len(l), 3), sorted_elements):
        l[idx] = val
    return l