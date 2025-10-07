from typing import List, Union

def split_words(text: str) -> Union[List[str], int]:
    if not (' ' not in text):  # if ' ' in text
        accumulator: List[str] = []
        idx = 0
        while idx < len(text):
            char = text[idx]
            if char == ' ':
                accumulator.append(text[:idx])
                text = text[idx + 1:]
                idx = -1
            idx += 1
        accumulator.append(text)
        return accumulator

    if not (' ,' not in text):  # if ' ' in text or ',' in text; but per pseudocode it checks only if ',' or ' ' in text
        buffer = ''
        pos = 0
        while pos < len(text):
            letter = text[pos]
            if letter == ',':
                buffer += ' '
            else:
                buffer += letter
            pos += 1
        segments: List[str] = []
        start = 0
        i = 0
        while i <= len(buffer):
            if i == len(buffer) or buffer[i] == ' ':
                segments.append(buffer[start:i])
                start = i + 1
            i += 1
        return segments

    characters: List[str] = []
    index = 0
    while index < len(text):
        symbol = text[index]
        ascii_val = ord(symbol)
        if ord('a') <= ascii_val <= ord('z') and ascii_val % 2 == 0:
            characters.append(symbol)
        index += 1
    return len(characters)