def main():
    # Read two lines of input from the user
    first_input = input()  # User input for the first line
    second_input = input()  # User input for the second line

    # Split the input strings into lists of strings
    first_tokens = first_input.split()  # Splitting by spaces
    second_tokens = second_input.split()  # Splitting by spaces

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the corresponding elements of the two lists
    for index in range(3):  # Assuming we compare the first 3 elements
        # Convert the token to an integer
        first_value = int(first_tokens[index])  # Convert to integer
        second_value = int(second_tokens[index])  # Convert to integer
        
        # Check if the values are different
        if first_value != second_value:  # Check for inequality
            difference_count += 1  # Increment the difference counter

    # Determine and print the result based on the number of differences
    if difference_count < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO otherwise

# Execute the main function
main()
