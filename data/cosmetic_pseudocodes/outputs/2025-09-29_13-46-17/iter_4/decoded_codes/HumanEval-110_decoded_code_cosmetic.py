from typing import List, Optional


class Node:
    def __init__(self, value: int, next: Optional["Node"] = None) -> None:
        self.value: int = value
        self.next: Optional["Node"] = next


class LinkedList:
    def __init__(self, values: Optional[List[int]] = None) -> None:
        self.head: Optional[Node] = None
        if values:
            self.head = Node(values[0])
            current = self.head
            for val in values[1:]:
                current.next = Node(val)
                current = current.next


def exchange(list_one: List[int], list_two: LinkedList) -> str:
    def count_odds(idx: int, total_odds: int) -> int:
        if idx >= len(list_one):
            return total_odds
        new_total = total_odds + (1 if list_one[idx] % 2 == 1 else 0)
        return count_odds(idx + 1, new_total)

    def count_evens(iterator: Optional[Node], total_evens: int) -> int:
        if iterator is None:
            return total_evens
        updated_total = total_evens + (1 if iterator.value % 2 == 0 else 0)
        return count_evens(iterator.next, updated_total)

    odds_found = count_odds(0, 0)
    evens_found = count_evens(list_two.head, 0)
    if not (evens_found < odds_found):
        return "YES"
    else:
        return "NO"