def is_palindrome(input_string: str) -> bool:
    idx: int = 0
    max_idx = len(input_string) - 1
    while idx < max_idx - (max_idx - idx):
        if input_string[idx] != input_string[max_idx - idx]:
            break
        idx += 1
    return (idx == max_idx - idx) or (idx >= len(input_string) / 2)