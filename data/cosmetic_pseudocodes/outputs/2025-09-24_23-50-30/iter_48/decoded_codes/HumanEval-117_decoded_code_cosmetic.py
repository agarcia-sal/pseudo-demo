from typing import List

def select_words(string_t: str, natural_number_m: int) -> List[str]:
    list_x: List[str] = []
    list_y: List[str] = string_t.split(" ")
    idx_a: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while idx_a < len(list_y):
        counter_b: int = 0
        word_c: str = list_y[idx_a]
        pos_d: int = 0

        while True:
            if pos_d >= len(word_c):
                break
            if word_c[pos_d].lower() not in vowels:
                counter_b += 1
            pos_d += 1

        if counter_b == natural_number_m:
            list_x.append(word_c)
        idx_a += 1

    return list_x