from typing import List


def file_name_check(parameter_filename: str) -> str:
    valid_extensions_collection: List[str] = ['txt', 'exe', 'dll']
    partitioned_segments = parameter_filename.split('.')
    while True:
        if len(partitioned_segments) != 2:
            break
        name, ext = partitioned_segments
        if ext not in valid_extensions_collection:
            break
        if len(name) == 0:
            break
        first_lett = name[0]
        if not (('A' <= first_lett <= 'Z') or ('a' <= first_lett <= 'z')):
            break
        num_digits_encountered = sum(1 for c in name if '0' <= c <= '9')
        if num_digits_encountered > 3:
            break
        return 'Yes'
    return 'No'