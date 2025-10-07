from typing import Dict, List


def fibfib(counter: int) -> int:
    if counter == 0 or counter == 1:
        return 0
    if counter == 2:
        return 1

    stack: List[int] = [counter]
    cache: Dict[int, int] = {0: 0, 1: 0, 2: 1}

    while stack:
        top = stack.pop()
        if top not in cache:
            if (top - 1) not in cache or (top - 2) not in cache or (top - 3) not in cache:
                stack.append(top)
                if (top - 1) not in cache:
                    stack.append(top - 1)
                if (top - 2) not in cache:
                    stack.append(top - 2)
                if (top - 3) not in cache:
                    stack.append(top - 3)
            else:
                cache[top] = cache[top - 1] + cache[top - 2] + cache[top - 3]

    return cache[counter]