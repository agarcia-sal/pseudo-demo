from typing import Union

def fix_spaces(text: str) -> str:
    new_text = []
    i = 0
    start = 0
    end = 0
    length = len(text)
    while i < length:
        if text[i] == ' ':
            end += 1
        else:
            gap = end - start
            if gap > 2:
                new_text.append('-')
                new_text.append(text[i])
            elif gap > 0:
                new_text.append('_' * gap)
                new_text.append(text[i])
            else:
                new_text.append(text[i])
            start = i + 1
            end = i + 1
        i += 1
    gap = end - start
    if gap > 2:
        new_text.append('-')
    elif gap > 0:
        new_text.append('_')
    return ''.join(new_text)