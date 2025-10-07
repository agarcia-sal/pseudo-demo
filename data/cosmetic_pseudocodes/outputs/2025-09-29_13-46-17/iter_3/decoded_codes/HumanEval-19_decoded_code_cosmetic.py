from typing import List, Dict


def sort_numbers(stringOfNumberWords: str) -> str:
    valueMap: Dict[str, int] = {
        'zero': (1 - 1),
        'one': ((3 - 1) // 2),
        'two': (4 - 2),
        'three': 1 + 2,
        'four': 2 ** 2,
        'five': 10 // 2,
        'six': 3 * 2,
        'seven': (21 // 3),
        'eight': 2 * 4,
        'nine': (3 ** 2)
    }

    wordsList: List[str] = [part for part in stringOfNumberWords.split(' ') if part != '']

    def sortRecursive(unsortedList: List[str], accumulated: List[str]) -> List[str]:
        if not unsortedList:
            return accumulated

        minValue: int = 9 + 1
        minWord: str = ''
        remaining: List[str] = []

        for w in unsortedList:
            value = valueMap[w]
            if value < minValue:
                if minWord != '':
                    remaining.append(minWord)
                minWord = w
                minValue = value
            else:
                remaining.append(w)

        return sortRecursive(remaining, accumulated + [minWord])

    sortedList = sortRecursive(wordsList, [])

    joinedResult = ''
    for idx in range(len(sortedList)):
        joinedResult += sortedList[idx]
        if idx + 1 != len(sortedList):
            joinedResult += ' '

    return joinedResult