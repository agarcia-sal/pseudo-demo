def sort_third(l):
    l = list(l)
    elements_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_elements = sorted(elements_divisible_by_three)
    for index in range(len(l)):
        if index % 3 == 0:
            l[index] = sorted_elements[index // 3]
    return l