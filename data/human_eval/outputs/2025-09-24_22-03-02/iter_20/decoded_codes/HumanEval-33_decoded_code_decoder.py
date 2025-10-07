from typing import List, Any

def sort_third(l: List[Any]) -> List[Any]:
    l = list(l)
    indices_divisible_by_three = []
    values_divisible_by_three = []
    for i in range(len(l)):
        if i % 3 == 0:
            indices_divisible_by_three.append(i)
            values_divisible_by_three.append(l[i])
    values_divisible_by_three = sorted(values_divisible_by_three)
    for j in range(len(indices_divisible_by_three)):
        l[indices_divisible_by_three[j]] = values_divisible_by_three[j]
    return l