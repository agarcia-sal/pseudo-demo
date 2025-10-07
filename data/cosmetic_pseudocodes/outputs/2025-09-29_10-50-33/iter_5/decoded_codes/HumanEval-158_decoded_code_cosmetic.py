from typing import List


def find_max(words_collection: List[str]) -> str:
    index_tracker: int = 0

    def sort_words() -> None:
        nonlocal index_tracker
        swapped_flag = True
        while swapped_flag:
            swapped_flag = False
            index_tracker = 0
            while index_tracker < len(words_collection) - 1:
                first_word = words_collection[index_tracker]
                second_word = words_collection[index_tracker + 1]
                unique_chars_first = len(set(first_word))
                unique_chars_second = len(set(second_word))

                # If NOT ((unique_chars_first > unique_chars_second) OR
                #          (unique_chars_first == unique_chars_second AND first_word <= second_word))
                if not (
                    (unique_chars_first > unique_chars_second)
                    or (unique_chars_first == unique_chars_second and first_word <= second_word)
                ):
                    words_collection[index_tracker] = second_word
                    words_collection[index_tracker + 1] = first_word
                    swapped_flag = True
                index_tracker += 1

    sort_words()
    return words_collection[0]