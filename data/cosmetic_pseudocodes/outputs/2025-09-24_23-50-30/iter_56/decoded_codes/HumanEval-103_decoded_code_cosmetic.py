from typing import Union


def rounded_avg(xu: int, yv: int) -> Union[int, str]:
    if yv < xu:
        return -1

    uz = 0
    # Loop from xu up to yv inclusive
    while xu <= yv:
        uz += xu
        xu += 1

    # Number of terms is yv - xu + 1 + 0, but xu incremented past yv, so recalc length properly
    # Since xu has been incremented past yv, count = (original yv - original xu + 1)
    # We lost original xu, so recompute count by uz and sum formula:
    # Alternative: Length is total numbers added, which is yv - original_xu +1.
    # We can recalculate count by subtracting uz sum formula approach is not needed 
    # But since xu changed, do it this way:
    # To fix, store original xu before the loop.
    # Let's redo with original variables

def rounded_avg(xu: int, yv: int) -> Union[int, str]:
    if yv < xu:
        return -1

    start = xu
    uz = 0
    while xu <= yv:
        uz += xu
        xu += 1

    count = yv - start + 1
    io = uz / count
    # Compute rj per condition: fractional_part = io + 0.5 modulo 1
    fractional_part = (io + 0.5) % 1
    if fractional_part < 0.5:
        rj = int((io + 0.5) // 1)  # floor(io + 0.5)
    else:
        rj = int(-(- (io - 0.5) // 1))  # ceil(io - 0.5), using math.ceil alternative

    kl = ""
    while True:
        if rj == 0:
            break
        kl = str(rj % 2) + kl
        rj //= 2

    return kl if kl != "" else "0"