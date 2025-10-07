from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def extract_digits_rec(tokens: List[str], accumulator: List[int]) -> List[int]:
        if not tokens:
            return accumulator
        current_token, *tail_tokens = tokens
        if not current_token.isdigit():
            return extract_digits_rec(tail_tokens, accumulator)
        return extract_digits_rec(tail_tokens, accumulator + [int(current_token)])

    splitted_tokens = string_description.split(' ')
    collected_numbers = extract_digits_rec(splitted_tokens, [])
    sum_of_collected = sum(collected_numbers)
    result = total_number_of_fruits - sum_of_collected
    return result