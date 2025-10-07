from collections import deque

def fizz_buzz(integer_n: int) -> int:
    queue_U: deque[int] = deque()
    index__Q: int = 0

    while index__Q < integer_n:
        # Enqueue index__Q if divisible by 11 or 13 (i.e., at least one modulo is zero)
        if not (index__Q % 11) * (index__Q % 13):
            queue_U.append(index__Q)
        index__Q += 1

    string_W: str = ""
    while queue_U:
        temp_X = queue_U.popleft()
        string_W += str(temp_X)

    accumulator_Y: int = 0
    iterator_Z: int = 0
    length_L: int = len(string_W)

    while iterator_Z < length_L:
        # Increment accumulator_Y if the character is '7'
        if not (string_W[iterator_Z] != '7'):
            accumulator_Y += 1
        iterator_Z += 1

    return accumulator_Y