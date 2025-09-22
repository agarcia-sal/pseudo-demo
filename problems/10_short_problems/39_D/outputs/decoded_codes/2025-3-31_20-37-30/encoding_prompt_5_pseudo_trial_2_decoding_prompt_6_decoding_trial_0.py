def main():
    # Gather input from the user
    first_input = input()  # Read first set of numbers
    second_input = input()  # Read second set of numbers
    
    # Split the input strings into lists of numbers
    first_list = first_input.split()  # Create a list of the first set of numbers
    second_list = second_input.split()  # Create a list of the second set of numbers
    
    # Initialize a variable to count differences
    difference_count = 0

    # Loop through each index of the lists (assuming both lists have exactly 3 elements)
    for index in range(3):  # Looping from index 0 to 2
        # Convert the current elements of both lists to integers
        first_value = int(first_list[index])  # Convert first list's current element to integer
        second_value = int(second_list[index])  # Convert second list's current element to integer
        
        # Check if the values at this index are different
        if first_value != second_value:
            # Increment the difference count
            difference_count += 1

    # After comparing all positions, decide on the output
    if difference_count < 3:
        print("YES")  # Output "YES" if fewer than 3 differences
    else:
        print("NO")  # Output "NO" if 3 or more differences

# Execute the main function only if this script is the main program
if __name__ == "__main__":
    main()
