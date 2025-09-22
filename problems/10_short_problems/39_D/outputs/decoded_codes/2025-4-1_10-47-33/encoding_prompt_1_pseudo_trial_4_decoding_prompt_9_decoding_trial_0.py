def main():
    # Prompt user for input and store in variables
    first_input = input()
    second_input = input()
    
    # Split inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    difference_count = 0  # Initialize counter for differences

    # Compare the elements of both lists up to the first three indices
    for index in range(3):
        # Convert string elements to integers for comparison
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])

        # Check if the values are different
        if value_from_first_list != value_from_second_list:
            difference_count += 1  # Increment difference count if not equal
    
    # Evaluate how many differences were found
    if difference_count < 3:
        print("YES")  # Fewer than three differences
    else:
        print("NO")   # Three or more differences

# Execute the main function
main()
