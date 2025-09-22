def main():
    # Get two input strings from the user
    first_input = input()  # Input first string of numbers
    second_input = input()  # Input second string of numbers
    
    # Split the input strings into lists of strings
    first_list = first_input.split()  # Convert first input string to list
    second_list = second_input.split()  # Convert second input string to list
    
    # Initialize a variable to count differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the elements at the current index to integers
        first_value = int(first_list[index])  # Convert current element in first list to integer
        second_value = int(second_list[index])  # Convert current element in second list to integer

        # If the values are different, increment the difference count
        if first_value != second_value:  # Check if values are not equal
            difference_count += 1  # Increment the difference count by 1

    # If the number of differences is less than 3, print "YES"; otherwise, print "NO"
    if difference_count < 3:  # Check if difference count is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Call the main function to execute the program
if __name__ == "__main__":  # Check if the program is being run directly
    main()  # Execute the main function
