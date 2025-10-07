from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    if not list_input:
        return list_input

    def helper_accumulate(lst: List[T], index: int, acc: List[T]) -> List[T]:
        if index >= len(lst):
            return acc
        if index % 3 == 0:
            return helper_accumulate(lst, index + 1, acc + [lst[index]])
        else:
            return helper_accumulate(lst, index + 1, acc)

    def helper_collect(lst: List[T], index: int) -> List[T]:
        if index >= len(lst):
            return []
        if index % 3 == 0:
            return [lst[index]] + helper_collect(lst, index + 1)
        else:
            return helper_collect(lst, index + 1)

    def helper_sort(lst: List[T]) -> List[T]:
        if not lst:
            return []
        head, tail = lst[0], lst[1:]
        sorted_tail = helper_sort(tail)
        result = []
        inserted = False
        i = 0
        while i < len(sorted_tail) and not inserted:
            if head <= sorted_tail[i]:
                result.extend([head] + sorted_tail[i:])
                inserted = True
            else:
                result.append(sorted_tail[i])
                i += 1
        if not inserted:
            result.append(head)
        return result

    copy_list = list_input[:]
    collected = helper_collect(copy_list, 0)
    sorted_collected = helper_sort(collected)
    idx = 0

    def reconstruct(acc: List[T]) -> List[T]:
        nonlocal idx
        if idx >= len(copy_list):
            return acc
        if idx % 3 == 0:
            acc1 = acc + [sorted_collected[idx // 3]]
            idx += 1
            return reconstruct(acc1)
        else:
            acc2 = acc + [copy_list[idx]]
            idx += 1
            return reconstruct(acc2)

    return reconstruct([])