from typing import List

def f(n_count: int) -> List[int]:
    container: List[int] = []
    for index in range(1, n_count + 1):
        if index % 2 == 0:
            fact_acc = 1
            for step in range(1, index + 1):
                fact_acc *= step
            container.append(fact_acc)
        else:
            sum_acc = 0
            for step in range(1, index + 1):
                sum_acc += step
            container.append(sum_acc)
    return container