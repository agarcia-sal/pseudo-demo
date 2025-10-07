from typing import List

def words_in_sentence(sentence: str) -> str:
    def compose_filtered_words(counter: int = 0, acc: List[str] = []) -> str:
        if counter >= len(sentence.split(" ")):
            return " ".join(acc)

        token = sentence.split(" ")[counter]
        mark = False

        if len(token) == 1:
            mark = True
        divisor = 2
        while divisor < len(token):
            if len(token) % divisor == 0:
                mark = True
            divisor += 1

        if not mark or len(token) == 2:
            acc = acc + [token]

        return compose_filtered_words(counter + 1, acc)

    return compose_filtered_words()