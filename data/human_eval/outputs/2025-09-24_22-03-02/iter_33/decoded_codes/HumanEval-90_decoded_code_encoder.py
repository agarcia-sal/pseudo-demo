def next_smallest(lst):
    unique_lst = []
    for i in range(len(lst)):
        current_element = lst[i]
        found = False
        for j in range(len(unique_lst)):
            if unique_lst[j] == current_element:
                found = True
                break
        if not found:
            unique_lst.append(current_element)
    sorted_lst = []
    while len(unique_lst) > 0:
        min_value = unique_lst[0]
        min_index = 0
        for k in range(1, len(unique_lst)):
            if unique_lst[k] < min_value:
                min_value = unique_lst[k]
                min_index = k
        sorted_lst.append(min_value)
        unique_lst.pop(min_index)
    if len(sorted_lst) < 2:
        return None
    else:
        return sorted_lst[1]