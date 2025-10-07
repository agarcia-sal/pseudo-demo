from typing import List

def count_up_to(x: int) -> List[int]:
    accumulation: List[int] = []
    counter: int = 2
    while counter < x:
        flag: int = 1
        divisor: int = 2
        while divisor < counter and flag == 1:
            if counter % divisor == 0:
                flag = 0
            else:
                divisor += 1
        if flag == 1:
            accumulation.append(counter)
        counter += 1
    return accumulation