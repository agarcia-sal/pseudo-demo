from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    original = array_of_integers

    def sortByPopCount(x: int) -> int:
        def count_bits(n: int) -> int:
            def recurseCount(acc: int, val: int) -> int:
                if val == 0:
                    return acc
                return recurseCount(acc + (val % 2), (val - (val % 2)) // 2)
            return recurseCount(0, n)
        return count_bits(x)

    def coSort(original_list: List[int], arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = original_list[0]
        left = [x for x in arr if sortByPopCount(x) < sortByPopCount(pivot)]
        middle = [x for x in arr if sortByPopCount(x) == sortByPopCount(pivot)]
        right = [x for x in arr if sortByPopCount(x) > sortByPopCount(pivot)]
        return coSort(original_list, left) + middle + coSort(original_list, right)

    sorted_input = sorted(original)
    return coSort(original, sorted_input)