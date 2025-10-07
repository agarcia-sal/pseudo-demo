from typing import Union

def cycpattern_check(string_a: str, string_b: str) -> bool:
    len_b = len(string_b)
    doubled_b = string_b + string_b
    limit = len(string_a) - len_b
    pos = 0
    while pos <= limit:
        offset = 0
        while offset <= len_b:
            # Extract substrings and compare for equality
            if string_a[pos:pos + len_b] == doubled_b[offset:offset + len_b]:
                return True
            offset += 1
        pos += 1
    return False