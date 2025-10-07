def median(l: list):
    l = sorted(l)
    length_l = len(l)
    remainder = length_l % 2
    if remainder == 1:
        index = length_l // 2
        result = l[index]
        return result
    else:
        index1 = (length_l // 2) - 1
        index2 = length_l // 2
        element1 = l[index1]
        element2 = l[index2]
        sum_elements = element1 + element2
        result = sum_elements / 2.0
        return result