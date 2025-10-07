from typing import List, Set

def common(list1: List[int], list2: List[int]) -> List[int]:
    def match(i: int, j: int, acc: Set[int]) -> Set[int]:
        if i == len(list1):
            if j == len(list2):
                return acc
            else:
                # If list1 is exhausted but list2 isn't, skip elements in list2
                return match(i, j + 1, acc)
        else:
            if j == len(list2):
                # Move to next element in list1 when list2 exhausted
                return match(i + 1, 0, acc)
            if list1[i] == list2[j]:
                return match(i, j + 1, acc | {list1[i]})
            else:
                return match(i, j + 1, acc)

    intersect_set = match(0, 0, set())

    def to_list(s: Set[int], length: int) -> List[int]:
        # Convert set to list by recursively building it (order not preserved)
        if length == 0:
            return []
        prev = to_list(s, length - 1)
        return prev + [list(s)[length - 1]]

    omega = to_list(intersect_set, len(intersect_set))

    def lis(seq: List[int], length: int) -> List[int]:
        # Longest Increasing Subsequence (LIS), O(n^2) recursive version
        if length == 1:
            return [seq[0]]
        prev_lis = lis(seq, length - 1)
        last_elem = prev_lis[-1]
        curr_elem = seq[length - 1]
        if last_elem <= curr_elem:
            return prev_lis + [curr_elem]
        else:
            # Replace element just before current position to possibly improve LIS
            return prev_lis[:-1] + [curr_elem]

    return lis(omega, len(omega))