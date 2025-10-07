from typing import Callable


def string_sequence(integer_n: int) -> str:
    def convert_and_accumulate(counter: int, limit: int, acc: str) -> str:
        if counter > limit:
            return acc
        updated_acc = str(counter) if acc == "" else acc + " " + str(counter)
        return convert_and_accumulate(counter + 1, limit, updated_acc)

    return convert_and_accumulate(0, integer_n, "")