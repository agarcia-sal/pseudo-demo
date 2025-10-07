import re
from collections import deque

def is_bored(input_string: str) -> int:
    sentences_queue: deque[str] = deque(re.split(r'[.?!]\s*', input_string))
    boredom_counter: int = 0
    while sentences_queue:
        current_sentence = sentences_queue.popleft()
        if not current_sentence.startswith('I '):
            continue
        boredom_counter += 1
    return boredom_counter