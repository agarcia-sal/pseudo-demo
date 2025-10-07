from typing import List

def sorted_list_sum(string_collection: List[str]) -> List[str]:
    def reorder_inplace(collection: List[str]) -> None:
        position: int = 0
        while position < len(collection):
            seeker: int = position + 1
            while seeker < len(collection):
                if collection[seeker] < collection[position]:
                    collection[position], collection[seeker] = collection[seeker], collection[position]
                seeker += 1
            position += 1

    reorder_inplace(string_collection)

    filtered_strings: List[str] = []
    checker: int = 0
    while checker < len(string_collection):
        if len(string_collection[checker]) % 2 == 0:
            filtered_strings.append(string_collection[checker])
        checker += 1

    def sort_by_length_asc(collection: List[str]) -> None:
        def swap(i: int, j: int) -> None:
            collection[i], collection[j] = collection[j], collection[i]

        outer: int = 0
        while outer < len(collection):
            inner: int = outer + 1
            while inner < len(collection):
                if len(collection[inner]) < len(collection[outer]):
                    swap(outer, inner)
                inner += 1
            outer += 1

    sort_by_length_asc(filtered_strings)

    return filtered_strings