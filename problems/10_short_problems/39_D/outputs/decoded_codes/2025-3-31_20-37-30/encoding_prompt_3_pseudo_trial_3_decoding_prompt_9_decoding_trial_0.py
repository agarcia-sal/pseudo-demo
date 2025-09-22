def main():
    # Step 1: Read input values
    first_input = input()
    second_input = input()

    # Step 2: Split inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a counter for non-matching elements
    mismatch_count = 0

    # Step 4: Compare elements in the lists
    for index in range(3):  # We are comparing only the first three elements
        # Step 5: Check for discrepancies
        # Ensure that we do not go out of range
        if index < len(first_list) and index < len(second_list):
            first_value = int(first_list[index])  # Convert first list value to integer
            second_value = int(second_list[index])  # Convert second list value to integer

            if first_value != second_value:
                mismatch_count += 1

    # Step 6: Output result based on the count of mismatches
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute main function
main()
