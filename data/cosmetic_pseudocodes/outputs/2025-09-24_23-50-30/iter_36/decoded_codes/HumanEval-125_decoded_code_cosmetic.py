from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    def contains_char(s: str, ch: str) -> bool:
        for idx in range(len(s)):
            if s[idx] == ch:
                return True
        return False

    if contains_char(text, ' '):
        tokens: List[str] = []
        start_index = 0

        def extract_tokens(s: str, pos: int) -> List[str]:
            nonlocal start_index
            if pos == len(s):
                segment = s[start_index:pos]
                if segment:
                    tokens.append(segment)
                return tokens

            if s[pos] == ' ':
                segment = s[start_index:pos]
                if segment:
                    tokens.append(segment)
                start_index = pos + 1
            return extract_tokens(s, pos + 1)

        return extract_tokens(text, 0)

    elif contains_char(text, ','):
        buffer: List[str] = []
        for pos in range(len(text)):
            if text[pos] == ',':
                buffer.append(' ')
            else:
                buffer.append(text[pos])

        replaced = ''.join(buffer)

        parts: List[str] = []
        segment_start = 0

        for pos in range(len(replaced) + 1):
            if pos == len(replaced) or replaced[pos] == ' ':
                segment = replaced[segment_start:pos]
                if segment:
                    parts.append(segment)
                segment_start = pos + 1

        return parts

    else:
        counter = 0
        for index in range(len(text)):
            char = text[index]
            ascii_code = ord(char)

            # char between 'a' and 'z' inclusive and ascii_code mod 2 == 0 (char is lowercase even ASCII)
            if 'a' <= char <= 'z' and (ascii_code % 2) == 0:
                counter += 1

        return counter