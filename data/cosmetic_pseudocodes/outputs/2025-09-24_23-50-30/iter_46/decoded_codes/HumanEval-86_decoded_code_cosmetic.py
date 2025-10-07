from typing import List


def anti_shuffle(meta_string: str) -> str:
    def recurse_words(memoed_list: List[str], remaining_words: List[str]) -> List[str]:
        if remaining_words:
            current_str = remaining_words[0]
            char_array = list(current_str)

            def recursive_sort(arr: List[str], left_idx: int) -> None:
                if left_idx < len(arr) - 1:

                    def inner_sort(k: int) -> None:
                        if k > left_idx:
                            if arr[k] < arr[k - 1]:
                                arr[k], arr[k - 1] = arr[k - 1], arr[k]
                                inner_sort(k - 1)
                            else:
                                inner_sort(k - 1)
                        else:
                            return

                    inner_sort(len(arr) - 1)
                    recursive_sort(arr, left_idx + 1)
                else:
                    return

            recursive_sort(char_array, 0)
            assembled_word = "".join(char_array)
            return recurse_words(memoed_list + [assembled_word], remaining_words[1:])
        else:
            return memoed_list

    processed_list = recurse_words([], meta_string.split(" "))
    acc_string = ""

    def assemble_string(lst: List[str], idx: int) -> None:
        nonlocal acc_string
        if idx < len(lst):
            if idx == 0:
                acc_string = lst[idx]
            else:
                acc_string += " " + lst[idx]
            assemble_string(lst, idx + 1)
        else:
            return

    assemble_string(processed_list, 0)
    return acc_string