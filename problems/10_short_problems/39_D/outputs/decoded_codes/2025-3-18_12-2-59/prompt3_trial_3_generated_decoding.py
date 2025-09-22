def main():
    # Step 1: Get input from the user
    first_input = input()
    second_input = input()

    # Step 2: Split the inputs into lists of string values
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a variable to track differences
    difference_count = 0

    # Step 4: Compare corresponding elements in both lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        # Convert string values to integers
        value_from_first = int(first_list[index])
        value_from_second = int(second_list[index])
        
        # Step 5: Check if they are different
        if value_from_first != value_from_second:
            difference_count += 1

    # Step 6: Determine the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function when the program runs
if __name__ == "__main__":
    main()
