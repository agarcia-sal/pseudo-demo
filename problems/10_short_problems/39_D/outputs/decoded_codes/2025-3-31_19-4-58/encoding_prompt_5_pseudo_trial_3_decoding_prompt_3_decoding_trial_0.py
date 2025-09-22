def main():
    # Read input values from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of values
    first_set = first_input.split()
    second_set = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Compare the numerical values from both sets
    for index in range(3):
        # Convert string values to integers
        first_value = int(first_set[index])
        second_value = int(second_set[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 
    
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # The sets differ in fewer than three positions
    else:
        print("NO")   # The sets differ in three or more positions

# Program execution starts here
main()
