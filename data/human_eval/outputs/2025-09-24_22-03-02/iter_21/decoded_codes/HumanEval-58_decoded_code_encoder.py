def common(l1: list, l2: list) -> list:
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    ret_list = []
    for element in ret:
        ret_list.append(element)
    ret_list_sorted = sorted(ret_list)
    return ret_list_sorted