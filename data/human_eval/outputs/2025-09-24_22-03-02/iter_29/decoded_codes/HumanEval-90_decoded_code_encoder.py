def next_smallest(lst):
    unique_set = []
    for i in range(len(lst)):
        found = False
        for j in range(len(unique_set)):
            if unique_set[j] == lst[i]:
                found = True
                break
        if not found:
            unique_set.append(lst[i])
    sorted_list = []
    while len(unique_set) > 0:
        min_value = unique_set[0]
        min_index = 0
        for k in range(1, len(unique_set)):
            if unique_set[k] < min_value:
                min_value = unique_set[k]
                min_index = k
        sorted_list.append(min_value)
        unique_set.pop(min_index)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]