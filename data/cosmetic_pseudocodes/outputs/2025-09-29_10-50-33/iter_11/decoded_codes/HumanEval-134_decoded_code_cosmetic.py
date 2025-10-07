from typing import List

def check_if_last_char_is_a_letter(input_string: str) -> bool:
    local_words: List[str] = []
    while True:
        local_words = input_string.split(" ")
        if len(local_words) > 0:
            break
        local_words = []
    char_candidate: str = local_words[-1]
    lower_char: str = char_candidate.lower()
    # Check if char_candidate is a single character and is a letter a-z
    if not (len(char_candidate) != 1 or (ord(lower_char) < 97 or ord(lower_char) > 122)):
        return True
    else:
        return False