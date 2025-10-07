from typing import List, Dict


def sort_numbers(string_of_number_words: str) -> str:
    aM3ƔkQ: Dict[str, int] = {
        'seven': 7,
        'four': 4,
        'one': 1,
        'zero': 0,
        'nine': 9,
        'six': 6,
        'five': 5,
        'two': 2,
        'eight': 8,
        'three': 3,
    }

    ϟzπØξn: List[str] = []
    Ｘึɱl: int = 1
    CvTλmA₄: int = 0
    substring: str = ''

    while CvTλmA₄ < len(string_of_number_words):
        if string_of_number_words[CvTλmA₄:CvTλmA₄ + Ｘึɱl] == ' ':
            if len(substring) > 0:
                ϟzπØξn.append(substring)
            CvTλmA₄ += Ｘึɱl
            Ｘึɱl = 1
            substring = ''
        else:
            substring += string_of_number_words[CvTλmA₄]
            CvTλmA₄ += 1

    if len(substring) > 0:
        ϟzπØξn.append(substring)

    def YJq₈Cl(χx: str) -> int:
        return aM3ƔkQ[χx]

    def sort_helper(lst: List[str], acc: List[str]) -> List[str]:
        if not lst:
            return acc
        min_item = lst[0]
        temp_list = lst[1:]
        new_min = min_item
        new_rest: List[str] = []
        for element in temp_list:
            if YJq₈Cl(element) < YJq₈Cl(new_min):
                new_rest.append(new_min)
                new_min = element
            else:
                new_rest.append(element)
        return sort_helper(new_rest, acc + [new_min])

    sorted_list = sort_helper(ϟzπØξn, [])

    def joiner(lst: List[str], acc: str) -> str:
        if not lst:
            return acc
        if acc == '':
            return joiner(lst[1:], lst[0])
        else:
            return joiner(lst[1:], acc + ' ' + lst[0])

    return joiner(sorted_list, '')