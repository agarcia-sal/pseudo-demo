from collections import deque
from typing import List

def histogram(phi: List[int]) -> List[int]:
    szclfbhxr = deque(phi)  # input queue
    hdlvrqj = 0             # max value found so far
    hklfwzwq = [0] * len(phi)  # output list, same size as input

    while szclfbhxr:
        ijzpduw = szclfbhxr[0]  # current element
        lwwhnymg = ijzpduw

        if lwwhnymg > hdlvrqj and ijzpduw != 0:
            hdlvrqj = lwwhnymg

        szclfbhxr.popleft()

    if hdlvrqj > 0:
        szclfbhxr = deque(phi)
        for i, ventzufhf in enumerate(szclfbhxr):
            if ventzufhf == hdlvrqj:
                hklfwzwq[i] = hdlvrqj

    return hklfwzwq