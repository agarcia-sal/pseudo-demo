def main():
    # Read two sets of input strings
    first_string = input()  # Read first input string
    second_string = input()  # Read second input string
    
    # Split the input strings into lists
    first_list = first_string.split()  # Split first string into a list
    second_list = second_string.split()  # Split second string into a list
    
    # Initialize a counter for differences
    difference_count = 0  
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert current list elements to integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check if the corresponding values are different
        if first_value != second_value:  # Check for inequality
            difference_count += 1  # Increment the difference count if they differ
    
    # Determine the result based on the count of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:  # Otherwise
        print("NO")  # Output NO

# Execute the main function
main()
