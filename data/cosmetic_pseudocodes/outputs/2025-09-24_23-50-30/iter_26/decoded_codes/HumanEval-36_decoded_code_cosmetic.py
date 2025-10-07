from typing import List


def fizz_buzz(integer_n: int) -> int:
    def accumulate_multiples(integer_p: int, collection_acc: List[int]) -> List[int]:
        if integer_p == integer_n:
            return collection_acc
        else:
            updated_acc = (
                collection_acc
                if (integer_p % 11 != 0 and integer_p % 13 != 0)
                else collection_acc + [integer_p]
            )
            return accumulate_multiples(integer_p + 1, updated_acc)

    def merge_numbers(collection_w: List[int]) -> str:
        def helper(idx: int, builder: str) -> str:
            if idx == len(collection_w):
                return builder
            else:
                return helper(idx + 1, builder + str(collection_w[idx]))

        return helper(0, "")

    def count_char(character_stream: str, tally: int) -> int:
        if not character_stream:
            return tally
        else:
            head, tail = character_stream[0], character_stream[1:]
            increment = 1 if head == "7" else 0
            return count_char(tail, tally + increment)

    multiples_list = accumulate_multiples(0, [])
    merged_str = merge_numbers(multiples_list)
    return count_char(merged_str, 0)