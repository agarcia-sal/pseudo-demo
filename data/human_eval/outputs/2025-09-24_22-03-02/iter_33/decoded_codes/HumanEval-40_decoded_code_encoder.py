def triples_sum_to_zero(l) -> bool:
    n = len(l)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            k = j + 1
            while k < n:
                sum_to_check = l[i] + l[j] + l[k]
                if sum_to_check == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False