def is_palindrome(check_str: str) -> bool:
    return check_str == check_str[::-1]


def make_palindrome(original_text: str) -> str:
    if original_text == "":
        return ""
    start_index = 0
    length = len(original_text)
    while not is_palindrome(original_text[start_index:length]):
        start_index += 1
    prefix_reversed = original_text[:start_index][::-1]
    return original_text + prefix_reversed