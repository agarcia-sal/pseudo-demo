from typing import List

def sort_numbers(magnitude_ciphertext: str) -> str:
    numeral_indexing: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    def parse_and_clean(input_str: str, accumulator: List[str], cursor: int) -> List[str]:
        if cursor == len(input_str):
            return accumulator
        start_pos = cursor
        while cursor < len(input_str) and input_str[cursor] != ' ':
            cursor += 1
        extracted = input_str[start_pos:cursor]
        if extracted:
            accumulator.append(extracted)
        while cursor < len(input_str) and input_str[cursor] == ' ':
            cursor += 1
        return parse_and_clean(input_str, accumulator, cursor)

    cleaned_tokens = parse_and_clean(magnitude_ciphertext, [], 0)

    def order_tokens(tokens_list: List[str], position: int) -> List[str]:
        if position >= len(tokens_list):
            return []
        pivot_word = tokens_list[position]

        def less_than_pivot(index: int, collected: List[str]) -> List[str]:
            if index >= len(tokens_list):
                return collected
            if numeral_indexing[tokens_list[index]] < numeral_indexing[pivot_word]:
                return less_than_pivot(index + 1, collected + [tokens_list[index]])
            else:
                return less_than_pivot(index + 1, collected)

        def not_less_than_pivot(index: int, collected: List[str]) -> List[str]:
            if index >= len(tokens_list):
                return collected
            if numeral_indexing[tokens_list[index]] >= numeral_indexing[pivot_word]:
                return not_less_than_pivot(index + 1, collected + [tokens_list[index]])
            else:
                return not_less_than_pivot(index + 1, collected)

        left_side = less_than_pivot(0, [])
        right_side = not_less_than_pivot(0, [])
        return order_tokens(left_side + right_side, position + 1)

    def quicksort(arr: List[str]) -> List[str]:
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less_equal = [x for x in arr[1:] if numeral_indexing[x] <= numeral_indexing[pivot]]
        greater = [x for x in arr[1:] if numeral_indexing[x] > numeral_indexing[pivot]]
        return quicksort(less_equal) + [pivot] + quicksort(greater)

    ordered_words = quicksort(cleaned_tokens)
    return ' '.join(ordered_words)