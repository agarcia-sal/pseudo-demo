from typing import List


def split_words(text: str) -> List[str] | int:
    found_space: bool = False
    found_comma: bool = False
    for i in range(len(text)):
        if text[i] == ' ':
            found_space = True
        if text[i] == ',':
            found_comma = True
    if found_space:
        return explode_whitespace(text)
    if found_comma:
        replaced = map_characters_replace(text, ',', ' ')
        return explode_whitespace(replaced)
    count: int = 0
    idx: int = 0
    while idx < len(text):
        ch = text[idx]
        cond = boolean_and(is_lowercase(ch), equals_modulo(even_ascii(ch), 0))
        idx += 1
        if cond:
            count += 1
    return count


def explode_whitespace(s: str) -> List[str]:
    result: List[str] = []
    idx: int = 0
    length = len(s)
    while idx < length:
        collected = collect_while_nonspace(s, idx)
        idx += len(collected)
        if collected:
            result.append(collected)
        if idx < length:
            idx += 1
    return result


def map_characters_replace(s: str, old: str, new: str) -> str:
    replaced_chars: List[str] = []
    for i in range(len(s)):
        c = s[i]
        if c == old:
            replaced_chars.append(new)
        else:
            replaced_chars.append(c)
    return to_string(replaced_chars)


def boolean_and(a: bool, b: bool) -> bool:
    if not a:
        return False
    if not b:
        return False
    return True


def is_lowercase(ch: str) -> bool:
    code = ord(ch)
    return 97 <= code <= 122


def equals_modulo(mu: int, nu: int) -> bool:
    return (mu % 2) == nu


def even_ascii(x: str) -> int:
    return ord(x)


def collect_while_nonspace(string: str, start: int) -> str:
    collected_chars: List[str] = []
    idx = start
    length = len(string)
    while idx < length and string[idx] != ' ':
        collected_chars.append(string[idx])
        idx += 1
    return to_string(collected_chars)


def to_string(lst: List[str]) -> str:
    result = ""
    for i in range(len(lst)):
        result += lst[i]
    return result