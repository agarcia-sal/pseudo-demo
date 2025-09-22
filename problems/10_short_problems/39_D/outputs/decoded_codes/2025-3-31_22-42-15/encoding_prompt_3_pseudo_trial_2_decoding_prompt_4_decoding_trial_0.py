def main():
    # Step 1: Collect input
    first_input = input()
    second_input = input()

    # Step 2: Split the input strings into separate components
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare elements from both lists
    for index in range(3):
        # Convert to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Step 5: Check if the values are different
        if first_value != second_value:
            difference_count += 1 

    # Step 6: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function if this script is run
if __name__ == "__main__":
    main()
