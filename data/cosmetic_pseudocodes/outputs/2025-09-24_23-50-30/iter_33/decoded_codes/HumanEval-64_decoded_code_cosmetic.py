from typing import Union

def vowels_count(phrase_param: Union[str, list[str]]) -> int:
    vowels_collection = "aeiouAEIOU"
    count_accumulator = 0
    # Iterate from index 1 to end (1-based indexing adapted to 0-based)
    for index_tracker in range(1, len(phrase_param)):
        current_symbol = phrase_param[index_tracker]
        count_accumulator += 1 if current_symbol in vowels_collection else 0
    # Check last character for 'y' or 'Y'
    if len(phrase_param) > 0 and phrase_param[-1] in ('y', 'Y'):
        count_accumulator += 1
    return count_accumulator