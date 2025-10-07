from typing import Mapping, List, Union


def check_dict_case(container: Mapping[object, object]) -> bool:
    nodes: List[object] = list(container.keys())
    if len(nodes) == 0:
        return False

    tag: str = "start"

    def traverse(nodelist: List[object], idx: int) -> None:
        nonlocal tag
        if idx == len(nodelist):
            return

        item = nodelist[idx]

        if not isinstance(item, str):
            tag = "mixed"
            return

        if tag == "start":
            if item.isupper():
                tag = "upper"
            elif item.islower():
                tag = "lower"
            else:
                return
        elif tag == "upper":
            if not item.isupper():
                tag = "mixed"
                return
        elif tag == "lower":
            if not item.islower():
                tag = "mixed"
                return
        else:
            return

        traverse(nodelist, idx + 1)

    traverse(nodes, 0)

    return tag == "upper" or tag == "lower"