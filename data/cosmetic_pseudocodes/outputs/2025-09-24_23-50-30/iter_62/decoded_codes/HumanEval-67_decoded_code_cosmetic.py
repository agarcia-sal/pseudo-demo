from typing import List


def fruit_distribution(alpha_bravo: str, charlie_delta: int) -> int:
    echo_foxtrot: List[int] = []

    def golf_hotel(india: str) -> int:
        if india == "":
            return 0
        juliet_kilo: List[str] = india.split(" ")

        def lima_mike(november: int, oscar: int) -> int:
            if oscar == len(juliet_kilo):
                return november
            papa_q: str = juliet_kilo[oscar]
            romeo_sierra: int = november
            if papa_q.isdigit():
                romeo_sierra = november + int(papa_q)
            return lima_mike(romeo_sierra, oscar + 1)

        return lima_mike(0, 0)

    tango_uniform: int = golf_hotel(alpha_bravo)
    return charlie_delta - tango_uniform