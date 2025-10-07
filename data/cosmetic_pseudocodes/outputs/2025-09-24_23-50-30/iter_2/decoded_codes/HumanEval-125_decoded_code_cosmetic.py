from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if not (' ' not in text and ',' not in text):
        if ' ' in text:
            return text.split()
        else:
            # Build replaced_text by iterating backwards over text,
            # replacing commas with spaces
            replaced_text = []
            for index in range(len(text) - 1, -1, -1):
                if text[index] == ',':
                    replaced_text.append(' ')
                else:
                    replaced_text.append(text[index])
            # reversed replaced_text is a list of chars, convert to string
            replaced_text_str = ''.join(replaced_text[::-1])
            return replaced_text_str.split()
    else:
        lowercase_chars: List[str] = []

        def recursive_check(pos: int, acc: int) -> int:
            if pos >= len(text):
                return acc
            current_char = text[pos]
            if current_char.islower() and (ord(current_char) % 2 == 0):
                return recursive_check(pos + 1, acc + 1)
            else:
                return recursive_check(pos + 1, acc)

        return recursive_check(0, 0)