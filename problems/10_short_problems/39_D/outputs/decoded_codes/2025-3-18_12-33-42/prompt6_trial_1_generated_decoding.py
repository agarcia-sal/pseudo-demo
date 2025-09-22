def main():
    # Get the first input string representing a list of three values
    first_input = input()
    
    # Get the second input string representing a list of three values
    second_input = input()
    
    # Split both input strings into lists of values
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the indices for the first three elements
    for index in range(3):
        # Convert the current elements from both lists to integers
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])
        
        # Compare the two values
        if value_from_first_list != value_from_second_list:
            # Increment the difference counter if they are not equal
            difference_count += 1 
    
    # Check the number of differences
    if difference_count < 3:
        # Print "YES" if differences are less than 3
        print("YES")
    else:
        # Print "NO" if differences are 3 or more
        print("NO")

# Entry point of the program
main()
