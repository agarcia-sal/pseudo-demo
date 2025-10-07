from typing import Dict, List


def fib(value: int) -> int:
    if value == 0:
        return 0
    if value == 1:
        return 1

    stack: List[int] = [value, value - 1, value - 2]
    results: Dict[int, int] = {}

    while stack:
        current = stack.pop()

        if current in results:
            continue

        if current == 0:
            results[0] = 0
        elif current == 1:
            results[1] = 1
        else:
            if (current - 1) not in results:
                stack.append(current)
                stack.append(current - 1)
                continue
            if (current - 2) not in results:
                stack.append(current)
                stack.append(current - 2)
                continue
            results[current] = results[current - 1] + results[current - 2]

    return results[value]