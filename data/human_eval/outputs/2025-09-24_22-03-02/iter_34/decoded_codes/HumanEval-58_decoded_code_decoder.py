def common(l1: list, l2: list) -> list:
    ret = set()
    index1 = 0
    while index1 < len(l1):
        e1 = l1[index1]
        index2 = 0
        while index2 < len(l2):
            e2 = l2[index2]
            if e1 == e2:
                ret.add(e1)
            index2 += 1
        index1 += 1
    ret_list = []
    for element in ret:
        ret_list.append(element)
    ret_list.sort()
    return ret_list