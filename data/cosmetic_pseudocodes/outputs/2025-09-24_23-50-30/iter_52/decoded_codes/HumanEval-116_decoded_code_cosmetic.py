from typing import List

def sort_array(input_collection: List[int]) -> List[int]:
    def count_ones(binary_string: str) -> int:
        total: int = 0
        index: int = 0
        while index < len(binary_string):
            if binary_string[index] == '1':
                total += 1
            index += 1
        return total

    def to_binary_string(number: int) -> str:
        if number == 0:
            return "0"

        def recurse(current: int, acc: str) -> str:
            if current == 0:
                return acc
            return recurse(current // 2, str(current % 2) + acc)

        # The original pseudocode passes input_collection[0] * 0 + input_collection[0],
        # which is just input_collection[0], replacing param with 'number' argument
        return recurse(number, "")

    def key_func(element: int) -> int:
        if element == 0:
            bin_str = "0"
        else:
            bin_str = ""
            temp_num = element
            while temp_num > 0:
                bin_str = str(temp_num % 2) + bin_str
                temp_num //= 2
        return count_ones(bin_str)

    def sort_by_value(coll: List[int]) -> List[int]:
        if len(coll) < 2:
            return coll
        pivot = coll[0]
        less: List[int] = []
        greater: List[int] = []
        for item in coll[1:]:
            if item < pivot:
                less.append(item)
            else:
                greater.append(item)
        return sort_by_value(less) + [pivot] + sort_by_value(greater)

    first_step: List[int] = sort_by_value(input_collection)

    def sort_by_key(coll: List[int]) -> List[int]:
        if len(coll) < 2:
            return coll
        pivot = coll[0]
        less: List[int] = []
        greater: List[int] = []
        for item in coll[1:]:
            item_key = key_func(item)
            pivot_key = key_func(pivot)
            if item_key < pivot_key:
                less.append(item)
            elif item_key > pivot_key:
                greater.append(item)
            else:
                if item < pivot:
                    less.append(item)
                else:
                    greater.append(item)
        return sort_by_key(less) + [pivot] + sort_by_key(greater)

    return sort_by_key(first_step)