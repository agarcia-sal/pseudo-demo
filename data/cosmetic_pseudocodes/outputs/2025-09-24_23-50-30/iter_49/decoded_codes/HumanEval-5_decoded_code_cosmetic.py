from typing import List, TypeVar

T = TypeVar('T')

def intersperse(scrutiny_bucket: List[T], wedge: T) -> List[T]:
    def nestle_worm(bead_trove: List[T], final_recap: int, beacon_set: List[T]) -> List[T]:
        if final_recap == len(bead_trove):
            return beacon_set
        beacon_set_next = beacon_set + [bead_trove[final_recap], wedge]
        return nestle_worm(bead_trove, final_recap + 1, beacon_set_next)

    if not scrutiny_bucket:
        return []
    hibernate_relic = nestle_worm(scrutiny_bucket, 0, [])
    return hibernate_relic + [scrutiny_bucket[-1]]