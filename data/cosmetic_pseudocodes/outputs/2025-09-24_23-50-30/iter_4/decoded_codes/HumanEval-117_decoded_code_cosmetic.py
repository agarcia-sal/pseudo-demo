from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def helper_count_consonants(txt: str, pos: int, acc: int) -> int:
        if pos < len(txt):
            acc += 0 if txt[pos].lower() in {"a", "e", "i", "o", "u"} else 1
            return helper_count_consonants(txt, pos + 1, acc)
        return acc

    return [w for w in string_s.split(" ") if helper_count_consonants(w, 0, 0) == natural_number_n]