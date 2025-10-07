def largest_divisor(h_number: int) -> int:
    index_tracker: int = h_number - 1
    while index_tracker > 0:
        remainder_result: int = h_number % index_tracker
        if remainder_result == 0:
            return index_tracker
        index_tracker -= 1
    # If no divisor other than h_number itself is found, return 1 as the smallest divisor
    return 1