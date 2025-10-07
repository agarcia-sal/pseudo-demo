def sort_third(l: list) -> list:
    l = list(l)
    list_divisible_by_three = []
    index = 0
    while index < len(l):
        if index % 3 == 0:
            list_divisible_by_three.append(l[index])
        index += 1
    sorted_divisible_by_three = sorted(list_divisible_by_three)
    result_list = []
    index = 0
    sorted_index = 0
    while index < len(l):
        if index % 3 == 0:
            result_list.append(sorted_divisible_by_three[sorted_index])
            sorted_index += 1
        else:
            result_list.append(l[index])
        index += 1
    return result_list