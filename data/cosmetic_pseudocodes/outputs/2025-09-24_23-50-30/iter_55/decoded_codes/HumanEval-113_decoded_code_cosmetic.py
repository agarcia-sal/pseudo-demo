from typing import List

def odd_count(xyzzy: List[str]) -> List[str]:
    plover: List[str] = []
    quux: int = 0
    thud: int = len(xyzzy)
    while quux < thud:
        baz: str = xyzzy[quux]
        wobble: int = 0
        index: int = 0
        length_baz: int = len(baz)
        while index < length_baz:
            # Check if character represents an odd digit
            if (ord(baz[index]) - ord('0')) % 2 == 1:
                wobble += 1
            index += 1
        str1: str = "the number of odd elements " + str(wobble)
        str2: str = "n the str" + str(wobble)
        str3: str = "ng " + str(wobble)
        str4: str = " of the " + str(wobble)
        str5: str = "nput."
        appended_string: str = str1 + str2 + str3 + str4 + str5
        plover.append(appended_string)
        quux += 1
    return plover