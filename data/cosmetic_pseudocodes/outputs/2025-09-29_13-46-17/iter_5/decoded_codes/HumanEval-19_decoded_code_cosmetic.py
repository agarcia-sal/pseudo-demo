from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    initial_value_map: dict[str, int] = {
        'seven': 7,
        'four': 4,
        'nine': 9,
        'six': 6,
        'eight': 8,
        'one': 1,
        'three': 3,
        'two': 2,
        'five': 5,
        'zero': 0,
    }

    def filter_nonempty_words(wordsList: List[str], index: int, accList: List[str]) -> List[str]:
        if index == len(wordsList):
            return accList
        else:
            if wordsList[index] != '':
                return filter_nonempty_words(wordsList, index + 1, accList + [wordsList[index]])
            else:
                return filter_nonempty_words(wordsList, index + 1, accList)

    temp_words: List[str] = string_of_number_words.split(' ')
    filtered_words: List[str] = filter_nonempty_words(temp_words, 0, [])

    def comparator(wordA: str, wordB: str) -> int:
        valA = initial_value_map[wordA]
        valB = initial_value_map[wordB]
        if valA > valB:
            return 1
        elif valA < valB:
            return -1
        else:
            return 0

    def sort_list(lst: List[str]) -> List[str]:
        if len(lst) <= 1:
            return lst
        pivot = lst[0]

        def less_than_pivot(acc: List[str], elem: str) -> List[str]:
            if initial_value_map[elem] < initial_value_map[pivot]:
                return acc + [elem]
            else:
                return acc

        def greater_equal_pivot(acc: List[str], elem: str) -> List[str]:
            if initial_value_map[elem] >= initial_value_map[pivot]:
                return acc + [elem]
            else:
                return acc

        less_than = []
        for e in lst[1:]:
            less_than = less_than_pivot(less_than, e)
        greater_equal = []
        for e in lst[1:]:
            greater_equal = greater_equal_pivot(greater_equal, e)

        return sort_list(less_than) + [pivot] + sort_list(greater_equal)

    sorted_list: List[str] = sort_list(filtered_words)

    answer = ''
    for idx in range(len(sorted_list)):
        if idx == 0:
            answer = sorted_list[idx]
        else:
            answer = answer + ' ' + sorted_list[idx]

    return answer