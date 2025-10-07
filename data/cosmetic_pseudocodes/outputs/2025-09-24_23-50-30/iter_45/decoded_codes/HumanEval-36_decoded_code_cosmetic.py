from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []

    def collect_multiples(index: int) -> None:
        if index >= integer_n:
            return
        # Append index if index is divisible by 11 or 13 (negation of "index mod 11 != 0 and index mod 13 != 0")
        if not (index % 11 != 0 and index % 13 != 0):
            collected_values.append(index)
        collect_multiples(index + 1)

    collect_multiples(0)

    combined_text: str = "".join(str(collected_values[pos]) for pos in range(len(collected_values)))

    def tally_sevens(position: int, acc: int) -> int:
        if position == len(combined_text):
            return acc
        return tally_sevens(position + 1, acc + (1 if combined_text[position] == "7" else 0))

    return tally_sevens(0, 0)