from typing import List


def largest_prime_factor(n: int) -> int:
    accumulator: int = 1
    candidates: List[int] = [x for x in range(2, n + 1)]
    filtered_candidates: List[int] = []

    for candidate_element in candidates:
        if n % candidate_element == 0:
            filtered_candidates.append(candidate_element)

    def check_prime(number: int) -> bool:
        if number <= 1:
            return False
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                return False
            divisor += 1
        return True

    for element in filtered_candidates:
        if check_prime(element) and element > accumulator:
            accumulator = element

    return accumulator