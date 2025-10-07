from collections import deque
from typing import Dict

def histogram(test_string_param: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_queue: deque[str] = deque(test_string_param.split(" "))
    max_freq: int = 0

    def find_max_frequency(queue_param: deque[str]) -> None:
        nonlocal max_freq
        if not queue_param:
            return
        current_element = queue_param.popleft()
        if current_element != "":
            def count_occurrences(q: deque[str], target: str) -> int:
                if not q:
                    return 0
                head = q.popleft()
                return (1 if head == target else 0) + count_occurrences(q, target)
            count_current = count_occurrences(deque(letters_queue), current_element)
            if max_freq < count_current:
                max_freq = count_current
        find_max_frequency(queue_param)

    find_max_frequency(deque(letters_queue))

    if max_freq > 0:
        length = len(letters_queue)
        for index in range(length):
            current_letter = letters_queue[index]
            if current_letter != "":
                freq_check = 0
                for counter in range(length):
                    if letters_queue[counter] == current_letter:
                        freq_check += 1
                if freq_check == max_freq:
                    freq_map[current_letter] = max_freq

    return freq_map