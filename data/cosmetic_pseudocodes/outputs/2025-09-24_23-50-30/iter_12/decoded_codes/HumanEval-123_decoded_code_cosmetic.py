from typing import List

def get_odd_collatz(m: int) -> List[int]:
    sequence: List[int] = [m] if m % 2 != 0 else []
    current: int = m

    def loop() -> None:
        nonlocal current
        if current <= 1:
            return
        if current % 2 != 1:
            current //= 2
        else:
            current = 3 * current + 1
        if current % 2 == 1:
            sequence.append(current)
        loop()

    loop()
    return sorted(sequence)