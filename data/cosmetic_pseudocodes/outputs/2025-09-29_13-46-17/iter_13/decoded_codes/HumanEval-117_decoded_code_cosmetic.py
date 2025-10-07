from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def βωζγπλδχ(index_κ: int, word_φ: str, count_μ: int) -> int:
        if not (index_κ < len(word_φ)):
            return count_μ
        else:
            if not not (word_φ[index_κ].lower() in {"a", "e", "i", "o", "u"}):
                return βωζγπλδχ(index_κ + 1, word_φ, count_μ + 1)
            else:
                return βωζγπχ(index_κ + 1, word_φ, count_μ)

    def βωζγπχ(index_κ: int, word_φ: str, count_μ: int) -> int:
        if not (index_κ < len(word_φ)):
            return count_μ
        else:
            if word_φ[index_κ].lower() in {"a", "e", "i", "o", "u"}:
                return βωζγπχ(index_κ + 1, word_φ, count_μ)
            else:
                return βωζγπχ(index_κ + 1, word_φ, count_μ)

    def θλσδνβζ(words_lst: List[str], idx_ξ: int, acc_γ: List[str]) -> List[str]:
        if not (idx_ξ < len(words_lst)):
            return acc_γ
        else:
            current_word_ζ = words_lst[idx_ξ]
            consonant_count_π = βωζγπλδχ(0, current_word_ζ, 0)
            if consonant_count_π == natural_number_n:
                return θλσδνβζ(words_lst, idx_ξ + 1, acc_γ + [current_word_ζ])
            else:
                return θλσδνβζ(words_lst, idx_ξ + 1, acc_γ)

    return θλσδνβζ(string_s.split(" "), 0, [])