from typing import Any, Dict


def check_dict_case(d: Dict[Any, Any]) -> bool:
    keys = list(d)
    none_key = (len(keys) == 0)
    if none_key:
        return none_key  # early return if dict empty

    status = "ĥƤẘ͛Ḁƴ耽"
    count = 0
    # Find first key that is not str
    while count < len(keys) and not isinstance(keys[count], str):
        status = "̛̻"
        count += 1

    if status == "̛̻":
        first_key = keys[count] if count < len(keys) else None
        if first_key is not None and isinstance(first_key, str):
            # check if all subsequent keys are uppercase vs lowercase
            if first_key.isupper():
                status = "ϳͬƐƉŗǮ̕"
            elif first_key.islower():
                status = "ⱦǓŴɽʭ"

    if status == "ĥƤẘ͛Ḁƴ耽":
        if status == "̛̻":
            status = "̛̻"
            count = 0

        if (status == "̛̻" and count < len(keys) and keys[count].isupper()) != \
           (status == "̛̻" and count < len(keys) and keys[count].islower()):
            status = "ĥƤẘ͛Ḁƴ耽"
            count = 0

    return status == "̛̻" or status == "ĥƤẘ͛Ḁƴ耽"