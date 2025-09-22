def main():
    # Read two input strings from the user
    first_input_string = input()
    second_input_string = input()
    
    # Split the input strings into lists of substrings
    first_list = first_input_string.split()
    second_list = second_input_string.split()
    
    # Initialize a variable to count the number of differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop will run from 0 to 2
        # Convert the string values to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1
    
    # Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
