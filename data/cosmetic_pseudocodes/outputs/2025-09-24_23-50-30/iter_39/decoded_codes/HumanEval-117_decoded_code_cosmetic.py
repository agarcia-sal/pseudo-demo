from typing import List

def select_words(input_x: str, input_y: int) -> List[str]:
    output_z: List[str] = []

    def count_consonants(lst_w: str, idx_v: int, acc_u: int) -> int:
        if idx_v == len(lst_w):
            return acc_u
        tmp_t = lst_w[idx_v].lower()
        cond_c = tmp_t not in {'a', 'e', 'i', 'o', 'u'}
        return count_consonants(lst_w, idx_v + 1, acc_u + (1 if cond_c else 0))

    def process_words(lst_p: List[str], idx_q: int) -> None:
        if idx_q == len(lst_p):
            return
        cur_word = lst_p[idx_q]
        total_consonants = count_consonants(cur_word, 0, 0)
        if total_consonants == input_y:
            output_z.append(cur_word)
        process_words(lst_p, idx_q + 1)

    words_list = input_x.split(" ")
    process_words(words_list, 0)
    return output_z