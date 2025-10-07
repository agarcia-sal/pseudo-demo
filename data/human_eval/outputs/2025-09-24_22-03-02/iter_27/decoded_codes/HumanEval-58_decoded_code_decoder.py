def common(l1: list, l2: list):
    ret = set()
    i = 0
    while i < len(l1):
        e1 = l1[i]
        j = 0
        while j < len(l2):
            e2 = l2[j]
            if e1 == e2:
                ret.add(e1)
            j += 1
        i += 1
    ret_list = []
    for element in ret:
        ret_list.append(element)
    sorted_ret_list = []
    while len(ret_list) > 0:
        min_index = 0
        k = 1
        while k < len(ret_list):
            if ret_list[k] < ret_list[min_index]:
                min_index = k
            k += 1
        sorted_ret_list.append(ret_list[min_index])
        ret_list.pop(min_index)
    return sorted_ret_list