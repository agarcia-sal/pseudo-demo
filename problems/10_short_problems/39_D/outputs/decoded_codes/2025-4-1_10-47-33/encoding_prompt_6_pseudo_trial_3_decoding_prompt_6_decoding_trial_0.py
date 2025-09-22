def do_main():
    # Step 1: Read input values.
    first_input = input()  # Read user input for the first sequence of numbers
    second_input = input()  # Read user input for the second sequence of numbers
    
    # Step 2: Split the input strings into lists of words.
    first_input_list = first_input.split()  # Split the first input by spaces
    second_input_list = second_input.split()  # Split the second input by spaces
    
    # Step 3: Initialize a counter for differences.
    difference_count = 0  # Counter for the number of differences
    
    # Step 4: Compare corresponding elements in both lists.
    for index in range(3):  # Loop through the first three elements
        # Convert string elements to integers for comparison.
        value_from_first_list = int(first_input_list[index])  # Convert to integer from first list
        value_from_second_list = int(second_input_list[index])  # Convert to integer from second list
        
        # Check if the values are different.
        if value_from_first_list != value_from_second_list:  # If values are not equal
            difference_count += 1  # Increment the difference counter
    
    # Step 5: Determine result based on the number of differences.
    if difference_count < 3:  # If less than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Main execution block.
if __name__ == "__main__":
    do_main()  # Call the do_main function
