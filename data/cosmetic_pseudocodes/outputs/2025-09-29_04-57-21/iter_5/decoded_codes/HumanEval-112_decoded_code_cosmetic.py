from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = [ch for ch in string_s if ch not in string_c]
    cleaned_str = ''.join(filtered_chars)
    return cleaned_str, cleaned_str == cleaned_str[::-1]