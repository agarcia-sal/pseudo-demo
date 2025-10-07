from typing import Set, List

def get_odd_collatz(n: int) -> List[int]:
    def tail_recursive_compute(x: int, accumulator: Set[int]) -> Set[int]:
        if not (x > 1):
            return accumulator
        updated_x = x // 2 if x % 2 == 0 else 3 * x + 1
        filtered_accumulator = accumulator | {updated_x} if updated_x % 2 != 0 else accumulator
        return tail_recursive_compute(updated_x, filtered_accumulator)

    initial_collection: Set[int] = set() if n % 2 == 0 else {n}
    ResultSet = tail_recursive_compute(n, initial_collection)

    def sorted_result(set_to_sort: Set[int]) -> List[int]:
        list_form: List[int] = []
        def iterate_items(to_sort: List[int], index: int) -> List[int]:
            if index == len(to_sort):
                return list_form
            list_form.append(to_sort[index])
            return iterate_items(to_sort, index + 1)

        unsorted_list = iterate_items(list(set_to_sort), 0)

        i = 0
        while i < len(unsorted_list) - 1:
            j = 0
            while j < len(unsorted_list) - i - 1:
                if unsorted_list[j] > unsorted_list[j + 1]:
                    unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                j += 1
            i += 1
        return unsorted_list

    return sorted_result(ResultSet)