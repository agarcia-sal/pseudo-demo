from typing import List

def odd_count(w: List[str]) -> List[str]:
    x: List[str] = []
    while True:
        if len(w) == 0:
            break
        y = w.pop(0)
        z = 0
        i = 0
        while i < len(y):
            if int(y[i]) % 2 == 1:
                z += 1
            i += 1
        a = "the number of odd elements "
        b = a + str(z)
        c = b + "n the str"
        d = c + str(z)
        e = d + "ng "
        f = e + str(z)
        g = f + " of the "
        h = g + str(z)
        final_str = h + "nput."
        x.append(final_str)
    return x