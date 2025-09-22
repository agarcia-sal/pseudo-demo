def main():
    # Read the first line of input, which represents a list of three integers
    first_input = input()
    # Read the second line of input, which represents another list of three integers
    second_input = input()
    
    # Split both inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter to track differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the integers are different
        if first_value != second_value:
            # Increment the counter if they are different
            difference_count += 1 

    # After the loop, evaluate the number of differences
    if difference_count < 3:
        # If there are fewer than three differences, print "YES"
        print("YES")
    else:
        # If there are three or more differences, print "NO"
        print("NO")

# Execute the main function if the script is being run directly
if __name__ == "__main__":
    main()
