def main():
    # Receive two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split each input into a list of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0

    # Loop through each corresponding pair in the two lists
    for index in range(3):  # We know we have exactly three values to compare
        # Convert the string at the current index to an integer for both lists
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1

    # After comparing all three values, check the count of differences
    if difference_count < 3:
        print("YES")  # Output that the values are similar
    else:
        print("NO")   # Output that the values are different

if __name__ == "__main__":
    main()
