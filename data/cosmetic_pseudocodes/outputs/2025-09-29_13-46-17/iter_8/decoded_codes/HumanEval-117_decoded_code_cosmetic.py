from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def _auxiliary(morpheme_rlq: List[str], gcbvw: int, accxqi: List[str]) -> List[str]:
        if not morpheme_rlq:
            return accxqi
        else:
            def count_consonants(fpxok: str, bzpkxo: int, poiwn: int) -> int:
                if bzpkxo < len(fpxok):
                    ch = fpxok[bzpkxo].lower()
                    poiwn2 = poiwn + (ch not in ("a", "e", "i", "o", "u"))
                    return count_consonants(fpxok, bzpkxo + 1, poiwn2)
                else:
                    return poiwn
            head_word = morpheme_rlq[0]
            tail_words = morpheme_rlq[1:]
            consonant_tally = count_consonants(head_word, 0, 0)
            new_acc = accxqi + [head_word] if consonant_tally == natural_number_n else accxqi
            return _auxiliary(tail_words, gcbvw + 1, new_acc)

    tokens = string_s.split(" ")
    return _auxiliary(tokens, 0, [])