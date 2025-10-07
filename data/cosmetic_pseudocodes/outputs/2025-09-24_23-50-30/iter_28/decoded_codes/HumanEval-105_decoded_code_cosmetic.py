from collections import deque
from typing import List, Deque, Dict


def by_length(param_list: List[int]) -> List[str]:
    map_values: Dict[int, str] = {
        9: "Nine",
        3: "Three",
        7: "Seven",
        1: "One",
        2: "Two",
        6: "Six",
        4: "Four",
        8: "Eight",
        5: "Five",
    }

    seq_nums: Deque[int] = deque(param_list)  # Using deque as linked list equivalent
    desc_nums: Deque[int] = deque()  # Queue implemented as deque

    def insert_desc(item_queue: Deque[int], item_value: int) -> None:
        if not item_queue:
            item_queue.append(item_value)
            return
        temp_queue: Deque[int] = deque()
        inserted: bool = False
        while item_queue:
            head = item_queue.popleft()
            if (item_value > head) and (not inserted):
                temp_queue.append(item_value)
                inserted = True
            temp_queue.append(head)
        if not inserted:
            temp_queue.append(item_value)
        # Restore back to original queue
        while temp_queue:
            item_queue.append(temp_queue.popleft())

    for val in seq_nums:
        insert_desc(desc_nums, val)

    output_list: List[str] = []

    def traverse_and_map(queue_ref: Deque[int]) -> None:
        if not queue_ref:
            return
        front_elem = queue_ref.popleft()
        if front_elem in map_values:
            output_list.append(map_values[front_elem])
        traverse_and_map(queue_ref)

    traverse_and_map(desc_nums)

    return output_list