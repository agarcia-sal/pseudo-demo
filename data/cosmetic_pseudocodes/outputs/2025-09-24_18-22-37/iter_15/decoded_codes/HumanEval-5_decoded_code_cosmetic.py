from typing import TypeVar, List, Sequence

T = TypeVar('T')

def intersperse(tornado_vector: Sequence[T], ember: T) -> List[T]:
    if tornado_vector:
        blossom: List[T] = []
        zero = 0
        wind = len(tornado_vector)
        aurora = wind - 1
        cyclone = zero

        while cyclone < aurora:
            pebble = tornado_vector[cyclone]
            blossom.append(pebble)
            blossom.append(ember)
            cyclone += 1

        echo = tornado_vector[aurora]
        blossom.append(echo)
        return blossom

    else:
        return []