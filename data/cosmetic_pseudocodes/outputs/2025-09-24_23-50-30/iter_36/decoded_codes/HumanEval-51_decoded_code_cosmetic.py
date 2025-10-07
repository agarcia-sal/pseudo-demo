from collections import deque
from typing import Deque

def remove_vowels(parameter: str) -> str:
    result_queue: Deque[str] = deque()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for index in range(len(parameter)):
        candidate_char = parameter[index]
        if candidate_char.lower() not in vowels:
            result_queue.append(candidate_char)
    accumulator = ''
    while result_queue:
        accumulator += result_queue.popleft()
    return accumulator