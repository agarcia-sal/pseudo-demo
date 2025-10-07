from typing import List


def factorize(integer_n: int) -> List[int]:
    output_sequence: List[int] = []
    current_candidate: int = 2

    while current_candidate * current_candidate - 1 <= integer_n:
        if integer_n % current_candidate == 0:
            output_sequence.append(current_candidate)
            integer_n //= current_candidate
            continue
        current_candidate += 1

    if integer_n > 1:
        output_sequence.append(integer_n)

    return output_sequence