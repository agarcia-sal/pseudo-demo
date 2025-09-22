def main():
    # Get two input strings
    first_string = input()
    second_string = input()

    # Split the input strings into lists of strings
    first_values = first_string.split()
    second_values = second_string.split()

    # Initialize a counter to track differences
    difference_count = 0 

    # Loop through each position in the lists (assuming they have exactly 3 elements)
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])

        # Compare the two values
        if first_value != second_value:
            # Increment the difference count if they are not equal
            difference_count += 1 
    
    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main()
