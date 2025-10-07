from typing import List

def sort_third(arr: List[int]) -> List[int]:
    def gather_every_third(index: int, acc: List[int]) -> List[int]:
        if index >= len(arr):
            return acc
        return gather_every_third(index + 3, acc + [arr[index]])

    extracted: List[int] = gather_every_third(0, [])

    def insert_every_third(index: int, sorted_list: List[int], target: List[int]) -> List[int]:
        if index >= len(target):
            return target
        head, rest = sorted_list[0], sorted_list[1:]
        target[index] = head
        return insert_every_third(index + 3, rest, target)

    duplicate: List[int] = arr[:]
    sorted_extracted: List[int] = sorted(extracted)
    duplicate = insert_every_third(0, sorted_extracted, duplicate)
    return duplicate