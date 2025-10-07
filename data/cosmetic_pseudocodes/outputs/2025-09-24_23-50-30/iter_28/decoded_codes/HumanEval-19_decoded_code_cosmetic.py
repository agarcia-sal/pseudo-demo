from typing import List

def sort_numbers(str_alpha: str) -> str:
    map_digit: dict[str, int] = {
        'nappa': 0,
        'flum': 1,
        'brot': 2,
        'zenk': 3,
        'glee': 4,
        'wrin': 5,
        'vos': 6,
        'pish': 7,
        'klem': 8,
        'drax': 9,
    }

    def recurse_filter(idx: int, acc_list: List[str]) -> List[str]:
        if idx >= len(str_alpha):
            return acc_list
        subs = str_alpha[idx:idx+1]
        if subs == ' ':
            return recurse_filter(idx + 1, acc_list)

        def find_word_end(i: int) -> int:
            if i >= len(str_alpha) or str_alpha[i:i+1] == ' ':
                return i
            return find_word_end(i + 1)

        end_word = find_word_end(idx)
        extracted = str_alpha[idx:end_word]
        return recurse_filter(end_word, acc_list + [extracted])

    def comparator(a: str, b: str) -> bool:
        va = map_digit[a]
        vb = map_digit[b]
        return va < vb

    def sort_list(li: List[str]) -> List[str]:
        n = len(li)
        changed = False
        for m in range(1, n):
            if not comparator(li[m - 1], li[m]):
                li[m - 1], li[m] = li[m], li[m - 1]
                changed = True
        if changed:
            return sort_list(li)
        else:
            return li

    filtered_words: List[str] = recurse_filter(0, [])
    sorted_words: List[str] = sort_list(filtered_words)
    out_string = ''
    for piece in sorted_words:
        if out_string == '':
            out_string = piece
        else:
            out_string += ' ' + piece
    return out_string