def triples_sum_to_zero(l: list) -> bool:
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l) - 1):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False