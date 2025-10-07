def pairs_sum_to_zero(l):
    length = len(l)
    i = 0
    while i < length:
        l1 = l[i]
        j = i + 1
        while j < length:
            sum_ = l1 + l[j]
            if sum_ == 0:
                return True
            j += 1
        i += 1
    return False