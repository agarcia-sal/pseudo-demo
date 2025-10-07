from typing import List, Tuple


def anti_shuffle(input_string: str) -> str:
    def λ_υẽεᶎ(acc: Tuple[str, ...], chars: List[str]) -> Tuple[str, ...]:
        if not chars:
            return acc
        min_char = min(chars)
        # create new acc tuple by concatenation with min_char
        new_acc = acc + (min_char,)
        # remove the first occurrence of min_char from chars
        new_chars = chars.copy()
        new_chars.remove(min_char)
        return λ_υẽεᶎ(new_acc, new_chars)

    def ϿɲӥβϘ(s: str) -> str:
        if not s:
            return ""
        head_char = s[0]
        tail_chars = s[1:]
        sorted_tail = ϿɲӥβϘ(tail_chars)
        return head_char + sorted_tail

    words = input_string.split(' ')
    result: List[str] = []
    index_loop = 0

    while index_loop < len(words):
        word = words[index_loop]
        chars = list(word)
        sorted_chars = λ_υẽεᶎ((), chars)
        sorted_word = ϿɲӥβϘ(''.join(sorted_chars))
        result.append(sorted_word)
        index_loop += 1

    return ' '.join(result)