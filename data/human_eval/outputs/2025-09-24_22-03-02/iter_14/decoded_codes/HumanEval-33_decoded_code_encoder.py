def sort_third(l: list) -> list:
    l = list(l)
    indices_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_divisible_by_three = sorted(indices_divisible_by_three)
    index_in_sorted = 0
    for index in range(len(l)):
        if index % 3 == 0:
            l[index] = sorted_divisible_by_three[index_in_sorted]
            index_in_sorted += 1
    return l