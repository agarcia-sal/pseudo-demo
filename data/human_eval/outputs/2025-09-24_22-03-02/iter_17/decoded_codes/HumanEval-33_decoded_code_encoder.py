def sort_third(l: list) -> list:
    l = list(l)
    temp_list = []
    index = 0
    while index < len(l):
        temp_list.append(l[index])
        index += 3
    sorted_list = sorted(temp_list)
    index = 0
    sorted_index = 0
    while index < len(l):
        l[index] = sorted_list[sorted_index]
        index += 3
        sorted_index += 1
    return l