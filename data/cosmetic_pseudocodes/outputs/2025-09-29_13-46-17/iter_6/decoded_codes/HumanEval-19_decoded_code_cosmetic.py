from typing import List, Tuple

def sort_numbers(string_of_number_words: str) -> str:
    dictionary_pairings: dict[str, int] = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0
    }

    def auxiliary_nonempty_words(accumulator: List[str], fragments: List[str], index: int) -> List[str]:
        if index == len(fragments):
            return accumulator
        current_fragment = fragments[index]
        adjusted_accumulator = accumulator + [current_fragment] if current_fragment != '' else accumulator
        return auxiliary_nonempty_words(adjusted_accumulator, fragments, index + 1)

    fragmented_tokens: List[str] = string_of_number_words.split(' ')
    words_collected: List[str] = auxiliary_nonempty_words([], fragmented_tokens, 0)

    def recurse_sort(unsorted: List[str], acc: List[str]) -> List[str]:
        if len(unsorted) == 0:
            return acc
        minimum = unsorted[0]
        rest = unsorted[1:]

        def find_minimum(c_list: List[str], c_min: str, c_rest: List[str], i: int) -> Tuple[str, List[str]]:
            if i == len(c_list):
                return c_min, c_rest
            element = c_list[i]
            if dictionary_pairings[element] < dictionary_pairings[c_min]:
                updated_min = element
                updated_rest = c_rest + [c_min]
            else:
                updated_min = c_min
                updated_rest = c_rest + [element]
            return find_minimum(c_list, updated_min, updated_rest, i + 1)

        candidate, residual = find_minimum(rest, minimum, [], 0)
        return recurse_sort(residual, acc + [candidate])

    reordered_list: List[str] = recurse_sort(words_collected, [])

    def join_with_space(arr: List[str], idx: int) -> str:
        if idx == len(arr):
            return ''
        sep = '' if idx == len(arr) - 1 else ' '
        return arr[idx] + sep + join_with_space(arr, idx + 1)

    final_string: str = join_with_space(reordered_list, 0)
    return final_string