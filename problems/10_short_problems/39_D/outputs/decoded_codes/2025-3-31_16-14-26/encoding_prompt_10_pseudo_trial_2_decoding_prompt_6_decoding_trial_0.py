def do_main():
    # Step 1: Get input from the user
    first_input = input()  # Input for the first list
    second_input = input()  # Input for the second list
    
    # Step 2: Split input strings into lists
    first_list = first_input.split()  # Splitting by whitespace
    second_list = second_input.split()  # Splitting by whitespace
    
    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter for the differences
    
    # Step 4: Compare corresponding elements from both lists
    for index in range(3):  # We assume there are exactly three elements to compare
        first_number = int(first_list[index])  # Convert to integer
        second_number = int(second_list[index])  # Convert to integer
        
        # Check if the elements are different
        if first_number != second_number:  # If the numbers are different
            difference_count += 1  # Increment the counter
    
    # Step 5: Determine the outcome based on the number of differences
    if difference_count < 3:  # If there are less than three differences
        print("YES")  # Output YES
    else:  # If there are three or more differences
        print("NO")  # Output NO

# Main execution
do_main()  # Call the main function to execute
