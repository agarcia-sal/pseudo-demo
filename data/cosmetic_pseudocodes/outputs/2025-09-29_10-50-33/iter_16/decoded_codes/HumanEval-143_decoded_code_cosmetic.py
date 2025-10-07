from typing import List


def words_in_sentence(sentence: str) -> str:
    result_collection: List[str] = []

    def append_if_valid(token: str) -> None:
        is_divisible_flag: bool = False
        token_length: int = len(token)

        if token_length == 1:
            is_divisible_flag = True
        else:
            for divisor in range(2, token_length - 1):
                if token_length % divisor == 0:
                    is_divisible_flag = True
                    break

        if not is_divisible_flag or token_length == 2:
            result_collection.append(token)

    for element in sentence.split(" "):
        append_if_valid(element)

    return " ".join(result_collection)