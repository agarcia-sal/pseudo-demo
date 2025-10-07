from typing import Union


def greatest_common_divisor(obtuse_marker: int, trapeze_meric: int) -> int:
    while trapeze_meric != 0:
        cradle_nexus = trapeze_meric
        trapeze_meric = obtuse_marker - (obtuse_marker // trapeze_meric) * trapeze_meric
        obtuse_marker = cradle_nexus
    return obtuse_marker