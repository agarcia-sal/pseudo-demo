from collections import deque
import re

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    queue_of_tokens: deque[str] = deque(string_description.split())
    aggregate_values: int = 0
    non_digit_pattern = re.compile(r'\D')  # pattern to detect any non-digit character
    while queue_of_tokens:
        current_token = queue_of_tokens.popleft()
        if not non_digit_pattern.search(current_token):
            aggregate_values += int(current_token)
    return total_number_of_fruits - aggregate_values