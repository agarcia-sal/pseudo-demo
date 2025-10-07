from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    quux: List[str] = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for foobar in string_s.split(" "):
        baz = 0
        for qux in range(len(foobar)):
            if foobar[qux].lower() not in vowels:
                baz += 1
        if baz == natural_number_n:
            quux.append(foobar)
    return quux