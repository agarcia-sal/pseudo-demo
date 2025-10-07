from typing import List


def fib(w1: int) -> int:
    if w1 == 0:
        return 0
    if w1 == 1:
        return 1

    class Frame:
        __slots__ = ('x', 'y', 'z')

        def __init__(self, x: int, y: int, z: int) -> None:
            self.x = x
            self.y = y
            self.z = z

    stack: List[Frame] = [Frame(x=w1, y=0, z=0)]
    result = 0

    while stack:
        frame = stack.pop()
        if frame.x == 0:
            temp = 0
        elif frame.x == 1:
            temp = 1
        else:
            if frame.y == 0:
                # Push current frame with y=1 to continue after fib(x-1)
                stack.append(Frame(x=frame.x, y=1, z=frame.z))
                # Push fib(x-1)
                stack.append(Frame(x=frame.x - 1, y=0, z=0))
                continue
            elif frame.y == 1:
                frame.y = 2
                # Return to this frame after fib(x-2)
                stack.append(frame)
                # Push fib(x-2)
                stack.append(Frame(x=frame.x - 2, y=0, z=0))
                continue
            else:
                temp = frame.z + result

        result = temp
        if stack:
            top = stack[-1]
            if top.y == 1:
                top.z = temp

    return result