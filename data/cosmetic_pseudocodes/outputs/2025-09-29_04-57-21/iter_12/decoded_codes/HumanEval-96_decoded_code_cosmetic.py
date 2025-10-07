from typing import List


def count_up_to(n: int) -> List[int]:
    prime_collection: List[int] = []
    candidate_index: int = 2

    while candidate_index < n:
        prime_flag: bool = True
        divisor_counter: int = 2

        while divisor_counter < candidate_index:
            if candidate_index % divisor_counter == 0:
                prime_flag = False
                break
            divisor_counter += 1

        if prime_flag:
            prime_collection.append(candidate_index)

        candidate_index += 1

    return prime_collection