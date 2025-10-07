from typing import List


def anti_shuffle(input_string: str) -> str:
    def process_words(words_list: List[str], accum_list: List[str], idx: int) -> List[str]:
        if idx >= len(words_list):
            return accum_list
        w = words_list[idx]
        c = list(w)

        def sort_array(arr: List[str], left: int, right: int) -> None:
            if left >= right:
                return
            i, j = left, right
            pivot = arr[(left + right) // 2]
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            sort_array(arr, left, j)
            sort_array(arr, i, right)

        sort_array(c, 0, len(c) - 1)
        sorted_w = ''.join(c)
        return process_words(words_list, accum_list + [sorted_w], idx + 1)

    words = input_string.split(' ')
    sorted_words = process_words(words, [], 0)
    output = ' '.join(sorted_words)
    return output