def main():
    # Prompt user for input
    first_set = input()
    second_set = input()
    
    # Split input strings into lists of strings
    first_list = first_set.split()
    second_list = second_set.split()

    # Initialize difference counter
    difference_count = 0

    # Check each position for differences
    for index in range(3):  # We expect exactly three integers in each set
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Count differences
        if first_value != second_value:
            difference_count += 1

    # Evaluate number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
if __name__ == "__main__":
    main()
