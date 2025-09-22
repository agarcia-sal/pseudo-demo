def main():
    # Read two input strings from the user
    first_string = input()
    second_string = input()
    
    # Split the input strings into a list of values
    values_from_first_string = first_string.split()
    values_from_second_string = second_string.split()
    
    # Initialize a counter to track differences
    difference_count = 0

    # Ensure we do not exceed the length of the lists
    for index in range(min(3, len(values_from_first_string), len(values_from_second_string))):
        # Convert the string values to integers
        value_from_first = int(values_from_first_string[index])
        value_from_second = int(values_from_second_string[index])

        # Check if the two values are different
        if value_from_first != value_from_second:
            # Increment the difference counter
            difference_count += 1 

    # If the count of differences is less than 3
    if difference_count < 3:
        print("YES")  # Output confirms that the two sets are similar
    else:
        print("NO")   # Output indicates significant differences

# Main execution point of the program
if __name__ == "__main__":
    main()
