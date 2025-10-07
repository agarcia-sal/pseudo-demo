def triples_sum_to_zero(l: list) -> bool:
    length = len(l)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            k = j + 1
            while k < length:
                if l[i] + l[j] + l[k] == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False