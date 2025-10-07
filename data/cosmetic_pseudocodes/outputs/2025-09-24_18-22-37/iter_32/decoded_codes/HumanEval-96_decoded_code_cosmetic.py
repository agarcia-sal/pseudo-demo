from typing import List

def count_up_to(x: int) -> List[int]:
    result: List[int] = []
    counter: int = 2

    while counter < x:
        prime_flag: bool = True
        divisor: int = 2

        while divisor < counter and prime_flag:
            if counter % divisor == 0:
                prime_flag = False
            else:
                divisor += 1

        if prime_flag:
            result.append(counter)

        counter += 1

    return result