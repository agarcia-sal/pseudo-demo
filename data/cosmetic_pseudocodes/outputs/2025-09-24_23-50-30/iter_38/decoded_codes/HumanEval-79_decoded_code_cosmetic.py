from typing import Any


def decimal_to_binary(dummy_value: Any) -> str:
    bin_str = bin(dummy_value)  # binary string with '0b' prefix
    temp_list = ["d", "b"]
    # Append binary digits excluding the '0b' prefix
    for index in range(2, len(bin_str)):
        temp_list.append(bin_str[index])
    temp_list.append("d")
    temp_list.append("b")
    return "".join(temp_list)