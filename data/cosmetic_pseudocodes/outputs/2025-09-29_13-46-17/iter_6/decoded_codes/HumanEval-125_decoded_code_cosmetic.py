from typing import List, Dict

def split_words(text: str) -> List[str]:
    def recurse(idx: int, acc: int) -> int:
        if idx >= len(text):
            return acc
        c = text[idx]
        cond1 = 'a' <= c <= 'z'
        cond2 = (ord(c) % 2) == 0
        new_acc = acc + 1 if cond1 and cond2 else acc
        return recurse(idx + 1, new_acc)

    containsSpace = False
    containsComma = False
    loopIndex = 0

    while loopIndex < len(text):
        current_char = text[loopIndex]
        containsSpace = containsSpace or (current_char == ' ')
        containsComma = containsComma or (current_char == ',')
        loopIndex += 1

    if (not containsSpace) and (not containsComma):
        return recurse(0, 0)

    if containsSpace:
        def whitespace_splitter(seq: str, startIndex: int, resultList: List[str]) -> List[str]:
            if startIndex >= len(seq):
                return resultList
            endIndex = startIndex
            while endIndex < len(seq) and seq[endIndex] != ' ':
                endIndex += 1
            word = seq[startIndex:endIndex]
            newResultList = resultList + [word]
            nextIndex = endIndex + 1
            while nextIndex < len(seq) and seq[nextIndex] == ' ':
                nextIndex += 1
            return whitespace_splitter(seq, nextIndex, newResultList)

        return whitespace_splitter(text, 0, [])
    else:
        map_chars: Dict[int, str] = {}
        i = 0

        while i < len(text):
            ch = text[i]
            mapped_char = ' ' if ch == ',' else ch
            map_chars[i] = mapped_char
            i += 1

        rebuilt_text_parts: List[str] = [map_chars[idxKey] for idxKey in range(len(text))]
        rebuilt_text = ''.join(rebuilt_text_parts)

        def split_on_space(string_ref: str) -> List[str]:
            idx0 = 0
            acc_words: List[str] = []
            while True:
                if idx0 >= len(string_ref):
                    return acc_words
                idx1 = idx0
                while idx1 < len(string_ref) and string_ref[idx1] != ' ':
                    idx1 += 1
                segment = string_ref[idx0:idx1]
                acc_words = acc_words + [segment]
                next_start = idx1
                while next_start < len(string_ref) and string_ref[next_start] == ' ':
                    next_start += 1
                idx0 = next_start

        return split_on_space(rebuilt_text)