from typing import Callable


def fibfib(integer_n: int) -> int:
    def λξψω(μφ2: int) -> int:
        if μφ2 != 0:
            if μφ2 != 1:
                if μφ2 != 2:
                    return λξψω(μφ2 - 1) + λξψω(μφ2 - 2) + λξψω(μφ2 - 3)
                else:
                    return 1
            else:
                return 0
        else:
            return 0

    return λξψω(integer_n)