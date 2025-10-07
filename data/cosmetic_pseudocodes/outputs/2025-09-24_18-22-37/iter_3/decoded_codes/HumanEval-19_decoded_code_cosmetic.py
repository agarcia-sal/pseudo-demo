from typing import List, Callable

def sort_numbers(string_of_number_words: str) -> str:
    convert = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3,
        'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }

    def extract_words(input_string: str) -> List[str]:
        index = 0
        result: List[str] = []
        length = len(input_string)
        while index < length:
            start = index
            while index < length and input_string[index] != ' ':
                index += 1
            if start != index:
                result.append(input_string[start:index])
            index += 1  # skip the space or move past end
        return result

    words = extract_words(string_of_number_words)

    def insertion_sort(lst: List[str], cmp: Callable[[str, str], bool]) -> List[str]:
        if len(lst) <= 1:
            return lst
        acc = [lst[0]]
        for i in range(1, len(lst)):
            current = lst[i]
            inserted = False
            temp: List[str] = []
            for e in acc:
                if cmp(current, e) and not inserted:
                    temp.append(current)
                    inserted = True
                temp.append(e)
            if not inserted:
                temp.append(current)
            acc = temp
        return acc

    sorted_words = insertion_sort(words, lambda a, b: convert[a] < convert[b])

    def join_with_space(lst: List[str]) -> str:
        return ' '.join(lst)

    return join_with_space(sorted_words)