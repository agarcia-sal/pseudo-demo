from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    else:
        if ',' in text:
            temp_text = text.replace(',', ' ')
            return temp_text.split()
        else:
            def count_lower_even_chars(chars: List[str], index: int, accumulator: int) -> int:
                if index >= len(chars):
                    return accumulator
                current_char = chars[index]
                is_lower_even = current_char.islower() and (ord(current_char) % 2 == 0)
                return count_lower_even_chars(chars, index + 1, accumulator + (1 if is_lower_even else 0))

            return count_lower_even_chars(list(text), 0, 0)