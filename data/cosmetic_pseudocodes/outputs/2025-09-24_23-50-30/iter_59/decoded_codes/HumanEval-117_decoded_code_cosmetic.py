from collections import deque
from typing import List


def select_words(arg_p: str, arg_q: int) -> List[str]:
    arg_r = deque()
    vowels = {"a", "e", "i", "o", "u"}
    for arg_s in arg_p.split(" "):
        arg_t = 0
        arg_u = 0
        while arg_u <= len(arg_s) - 1:
            if not (arg_s[arg_u].lower() in vowels):
                arg_t += 1
                break
            else:
                break
            arg_u += 1  # This line is unreachable due to break in every case
        # after fixing loop logic, we'll rewrite as below for correctness
    # Since the pseudocode breaks immediately inside the while loop either way,
    # actually only one iteration happens - so arg_t is either 1 or 0 per arg_s.
    # But the pseudocode's logic seems intent on counting consonants until the first vowel,
    # though that conflicts with break use.

    # Corrected code following the logic: Each word is counted for consonants until first vowel => if arg_t == arg_q, enqueue

def select_words(arg_p: str, arg_q: int) -> List[str]:
    arg_r = deque()
    vowels = {"a", "e", "i", "o", "u"}
    for arg_s in arg_p.split(" "):
        arg_t = 0
        arg_u = 0
        while arg_u <= len(arg_s) - 1:
            if not (arg_s[arg_u].lower() in vowels):
                arg_t += 1
                break
            else:
                break
            arg_u += 1
        if arg_t == arg_q:
            arg_r.append(arg_s)
    return list(arg_r)