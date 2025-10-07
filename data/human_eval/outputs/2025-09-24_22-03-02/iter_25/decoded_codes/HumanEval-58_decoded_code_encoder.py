def common(l1: list, l2: list) -> list:
    ret = set()
    for i in range(len(l1)):
        e1 = l1[i]
        for j in range(len(l2)):
            e2 = l2[j]
            if e1 == e2:
                ret.add(e1)
    ret_list = [None]
    for k in range(len(ret)):
        element_found = False
        for each_element in ret:
            if not element_found:
                ret_list.append(each_element)
                element_found = True
    ret_list.sort()
    return ret_list