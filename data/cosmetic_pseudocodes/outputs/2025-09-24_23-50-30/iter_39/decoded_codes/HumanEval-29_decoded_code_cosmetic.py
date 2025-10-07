from typing import List

def filter_by_prefix(sequence_of_tokens: List[str], key_substring: str) -> List[str]:
    collector: List[str] = []
    index: int = 0
    length_key = len(key_substring)
    while index < len(sequence_of_tokens):
        # If the token starts with key_substring, append it
        if sequence_of_tokens[index][:length_key] == key_substring:
            collector.append(sequence_of_tokens[index])
        index += 1
    return collector