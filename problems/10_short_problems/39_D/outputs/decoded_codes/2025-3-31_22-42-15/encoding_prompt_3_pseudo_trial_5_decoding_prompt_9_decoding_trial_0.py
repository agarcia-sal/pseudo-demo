def main():
    # Step 1: Gather input data
    first_input = input()
    second_input = input()

    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the two values are different
        if first_value != second_value:
            difference_count += 1  # Increment difference count

    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
if __name__ == "__main__":
    main()
