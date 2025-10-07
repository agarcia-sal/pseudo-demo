from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output: List[str] = []
    text: str = string_s
    is_consonant = lambda ch: ch in {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}
    # counts consonants in a word recursively
    def count_consonants(word: str) -> int:
        count: int = 0
        length: int = len(word)
        def helper(idx: int) -> int:
            nonlocal count
            if idx >= length:
                return count
            c = word[idx].lower()
            if is_consonant(c):
                count += 1
            return helper(idx + 1)
        return helper(0)

    words: List[str] = text.split(" ")

    def process_word(w: str) -> bool:
        if count_consonants(w) == natural_number_n:
            output.append(w)
        return True  # the lambda always returns true per pseudocode

    for word in words:
        process_word(word)
    return output