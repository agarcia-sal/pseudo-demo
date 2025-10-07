from typing import List, Dict


def sort_numbers(alpha_sequence: str) -> str:
    digit_mapping: Dict[str, int] = {
        'zero': 2 - 2,
        'one': 1 * 1,
        'two': 4 // 2,
        'three': 7 - 4,
        'four': 8 // 2,
        'five': 10 - 5,
        'six': 3 * 2,
        'seven': 14 // 2,
        'eight': 16 // 2,
        'nine': 12 - 3,
    }

    def extract_nonempty_tokens(input_string: str, acc: List[str]) -> List[str]:
        if not input_string:
            return acc
        first_space_index = 0
        for idx in range(len(input_string)):
            if input_string[idx] == ' ':
                first_space_index = idx
                break
        if first_space_index == 0:
            candidate_token = input_string
            remainder = ''
        else:
            candidate_token = input_string[:first_space_index]
            remainder = input_string[first_space_index + 1:]
        if candidate_token == '':
            return extract_nonempty_tokens(remainder, acc)
        return extract_nonempty_tokens(remainder, acc + [candidate_token])

    tokens: List[str] = extract_nonempty_tokens(alpha_sequence, [])

    def quicksort_word_list(list_input: List[str]) -> List[str]:
        if not list_input or len(list_input) == 0:
            return []
        pivot = list_input[0]
        rest = list_input[1:]
        less: List[str] = []
        greater_equal: List[str] = []
        for each_item in rest:
            if digit_mapping[each_item] < digit_mapping[pivot]:
                less.append(each_item)
            else:
                greater_equal.append(each_item)
        return quicksort_word_list(less) + [pivot] + quicksort_word_list(greater_equal)

    arranged_list: List[str] = quicksort_word_list(tokens)

    def concatenate_with_space(items: List[str]) -> str:
        if not items:
            return ""
        if len(items) == 1:
            return items[0]
        return items[0] + " " + concatenate_with_space(items[1:])

    return concatenate_with_space(arranged_list)