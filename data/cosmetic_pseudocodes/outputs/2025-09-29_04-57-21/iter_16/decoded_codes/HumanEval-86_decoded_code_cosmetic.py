from typing import Iterator

def anti_shuffle(input_string: str) -> str:
    words_collection = input_string.split(" ")
    sorted_collection: list[str] = []

    iterator: Iterator[str] = iter(words_collection)
    while True:
        try:
            current_word = next(iterator)
        except StopIteration:
            break

        chars_arr = list(current_word)

        index_i = 0
        while index_i < len(chars_arr) - 1:
            index_j = index_i + 1
            while index_j < len(chars_arr):
                if chars_arr[index_i] > chars_arr[index_j]:
                    chars_arr[index_i], chars_arr[index_j] = chars_arr[index_j], chars_arr[index_i]
                index_j += 1
            index_i += 1

        reconstructed_word = "".join(chars_arr)
        sorted_collection.append(reconstructed_word)

    output_str = ""
    first_flag = True
    for elem in sorted_collection:
        if not first_flag:
            output_str += " "
        else:
            first_flag = False
        output_str += elem

    return output_str