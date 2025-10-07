def common(l1, l2):
    # Convert l2 to a set for O(1) lookups to improve efficiency
    l2_set = set(l2)
    ret = set()

    for element in l1:
        if element in l2_set:
            ret.add(element)

    return sorted(ret)