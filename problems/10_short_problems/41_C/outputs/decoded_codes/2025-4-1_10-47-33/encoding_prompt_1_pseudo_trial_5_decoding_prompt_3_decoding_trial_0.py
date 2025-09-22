def process_input_string():
    # Step 1: Read Input
    input_string = input()

    # Step 2: Replace Keywords
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Handle Special Case for Initial Character
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]

    # Step 4: Initialize Variables
    at_count = 0
    result_list = []

    # Step 5: Handle Special Case for Email Format
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Step 6: Process Each Character
    for current_char in input_string:
        if current_char == "@":
            if at_count > 0:
                result_list.append("at")  # Append "at" for subsequent occurrences
            else:
                result_list.append(current_char)  # Append the first occurrence of "@"
            at_count += 1
        else:
            result_list.append(current_char)

    # Step 7: Combine Results
    output_string = ''.join(result_list)

    # Step 8: Handle Ending Special Case
    if output_string.endswith("."):
        output_string = output_string[:-1] + "dot"

    # Step 9: Output Result
    print(output_string)

# You can call the function to test it
process_input_string()
