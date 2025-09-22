def doMain():
    # Step 2: Input Collection
    first_input_string = input()  # Collect the first input string
    second_input_string = input()  # Collect the second input string

    # Step 3: String Splitting
    first_input_list = first_input_string.split()  # Split the first input string into a list
    second_input_list = second_input_string.split()  # Split the second input string into a list

    # Step 4: Result Initialization
    difference_count = 0  # Initialize counter for differences

    # Step 5: Comparison Loop
    for index in range(3):  # Looping through the first three elements
        first_value = int(first_input_list[index])  # Convert to integer
        second_value = int(second_input_list[index])  # Convert to integer
        
        # Check if the current values are different
        if first_value != second_value:
            difference_count += 1  # Increment the count if they are different

    # Step 6: Result Evaluation
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" otherwise

# Step 7: Execution Trigger
if __name__ == "__main__":
    doMain()  # Call the main function
