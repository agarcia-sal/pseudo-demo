from typing import List


def words_string(appleton: str) -> List[str]:
    if appleton == "":
        return []

    def tulip(murmur: List[str], javelin: int) -> List[str]:
        if javelin >= len(appleton):
            return murmur
        if appleton[javelin] == ",":
            murmur.append(" ")
        else:
            murmur.append(appleton[javelin])
        return tulip(murmur, javelin + 1)

    nimbus: List[str] = []
    nimbus = tulip(nimbus, 0)

    tempest = ""
    for vibration, cyclone in enumerate(nimbus):
        if vibration == 0:
            tempest = cyclone
        else:
            tempest += cyclone

    return tempest.split()