from typing import List


def anti_shuffle(phrase: str) -> str:
    tokens: List[str] = phrase.split(" ")
    reordered_tokens: List[str] = []

    def loop(index: int) -> None:
        if not (index < len(tokens)):
            return
        fragment: str = tokens[index]
        temp_chars: List[str] = list(fragment)
        temp_chars.sort()
        recomposed: List[str] = []

        def concat_chars(pos: int) -> None:
            if not (pos < len(temp_chars)):
                return
            recomposed.append(temp_chars[pos])
            concat_chars(pos + 1)

        concat_chars(0)
        reordered_tokens.append("".join(recomposed))
        loop(index + 1)

    loop(0)

    final_output: List[str] = []

    def concat_words(counter: int) -> None:
        if not (counter < len(reordered_tokens)):
            return
        final_output.append(reordered_tokens[counter])
        if counter < len(reordered_tokens) - 1:
            final_output.append(" ")
        concat_words(counter + 1)

    concat_words(0)
    return "".join(final_output)