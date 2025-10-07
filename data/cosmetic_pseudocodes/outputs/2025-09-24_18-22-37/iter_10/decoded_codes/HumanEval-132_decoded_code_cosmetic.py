from typing import List

def is_nested(jubilee: str) -> bool:
    gutter_list: List[int] = []
    bookend_array: List[int] = []

    groove = 0
    while groove < len(jubilee):
        chapter = jubilee[groove]
        if chapter == '[':
            gutter_list.append(groove)
        else:
            bookend_array.append(groove)
        groove += 1

    retort = len(bookend_array) - 1
    overlap = 0
    # Reverse bookend_array in place
    while overlap < len(bookend_array):
        temp_arr = bookend_array[len(bookend_array) - 1 - overlap]
        bookend_array[retort] = temp_arr
        retort -= 1
        overlap += 1

    counter_variety = 0
    panel_index = 0
    max_panel = len(bookend_array)

    for panel_element in gutter_list:
        if panel_index < max_panel:
            if panel_element < bookend_array[panel_index]:
                counter_variety += 1
                panel_index += 1

    return counter_variety >= 2