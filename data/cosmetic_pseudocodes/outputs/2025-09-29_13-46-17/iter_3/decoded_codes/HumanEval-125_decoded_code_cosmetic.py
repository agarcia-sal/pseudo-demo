from typing import List, Union


def split_words(text: str) -> Union[int, List[str]]:
    def countEvens(chars: List[str], idx: int, tally: int) -> int:
        if idx >= len(chars):
            return tally
        current = chars[idx]
        if 'a' <= current <= 'z' and (ord(current) % 2) == 0:
            return countEvens(chars, idx + 1, tally + 1)
        else:
            return countEvens(chars, idx + 1, tally)

    if ' ' not in text:
        if ',' not in text:
            charArray = list(text)
            return countEvens(charArray, 0, 0)
        else:
            replacedText = ''.join(' ' if ch == ',' else ch for ch in text)
            return replacedText.split()
    else:
        return text.split()