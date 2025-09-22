def main():
    # Read two lines of input representing two sets of three integers
    first_input = input()  # Example: "1 2 3"
    second_input = input()  # Example: "1 4 3"
    
    # Split the input strings into lists of strings
    first_list = first_input.split()  # Splits by space
    second_list = second_input.split()  # Splits by space
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the string values to integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1
            
    # Check the count of differences and print results
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
