def common(list1, list2):
    ret = set()
    for e1 in list1:
        for e2 in list2:
            if e1 == e2:
                ret.add(e1)
    return sorted(ret)