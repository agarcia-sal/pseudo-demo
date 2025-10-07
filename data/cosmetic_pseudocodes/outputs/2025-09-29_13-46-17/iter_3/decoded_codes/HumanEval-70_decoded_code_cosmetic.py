from typing import List


def strange_sort_list(listOfIntegers: List[int]) -> List[int]:
    def helper(remainingItems: List[int], flag: bool, acc: List[int]) -> List[int]:
        if not remainingItems:
            return acc
        selectedValue = min(remainingItems) if flag else max(remainingItems)
        filteredItems = []
        selected_count = 0
        for element in remainingItems:
            if element != selectedValue or selected_count >= 1:
                filteredItems.append(element)
            else:
                selected_count += 1
        return helper(filteredItems, not flag, acc + [selectedValue])

    return helper(listOfIntegers, True, [])