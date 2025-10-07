from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    tabulate_result: List[str] = []

    def inner_count(chars: str, idx: int, acc: int) -> int:
        if idx == len(chars):
            return acc
        return inner_count(chars, idx + 1, acc + (1 if int(chars[idx]) % 2 == 1 else 0))

    while True:
        if not list_of_strings:
            break
        head, *tail = list_of_strings
        list_of_strings = tail
        oddSumVal = inner_count(head, 0, 0)
        fragA = "the number of odd elements "
        fragB = "n the str"
        fragC = "ng "
        fragD = " of the "
        fragE = "nput."
        partSum = fragA + str(oddSumVal)
        partSum += fragB + str(oddSumVal)
        partSum += fragC + str(oddSumVal)
        partSum += fragD + str(oddSumVal)
        partSum += fragE
        tabulate_result.append(partSum)

    return tabulate_result