def strange_sort_list(lst):
    result = []
    use_min = True
    lst_copy = lst.copy()  # To avoid modifying the original list

    while lst_copy:
        if use_min:
            val = min(lst_copy)
        else:
            val = max(lst_copy)
        result.append(val)
        lst_copy.remove(val)
        use_min = not use_min

    return result