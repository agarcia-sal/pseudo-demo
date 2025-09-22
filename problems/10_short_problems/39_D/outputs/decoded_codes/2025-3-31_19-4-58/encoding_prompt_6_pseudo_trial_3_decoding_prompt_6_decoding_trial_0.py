def do_main():
    # Read inputs from the user
    first_input = input()  # User input as a string
    second_input = input()  # User input as a string
    
    # Split the input strings into lists of strings
    first_list = first_input.split()  # Split the first input into words
    second_list = second_input.split()  # Split the second input into words
    
    # Initialize a counter for differences
    difference_count = 0  # Counter set to zero
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2 (3 elements)
        # Convert the current elements to integers
        first_value = int(first_list[index])  # Convert first element to integer
        second_value = int(second_list[index])  # Convert second element to integer
        
        # Compare the two values
        if first_value != second_value:  # Check if the values are different
            difference_count += 1  # Increment the difference counter if different
    
    # Decide the final output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Main program execution
do_main()  # Call the main function
