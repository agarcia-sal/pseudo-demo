def main():
    # Get input from the user for the first set of numbers
    first_set = input()
    # Get input from the user for the second set of numbers
    second_set = input()
    
    # Split the input strings into lists of numbers
    first_numbers = first_set.split()
    second_numbers = second_set.split()
    
    # Initialize a counter for differences
    difference_count = 0

    # Compare corresponding numbers from both lists
    for index in range(3):  # Assuming there are always three numbers
        # Convert the strings to integers for comparison
        number_from_first_set = int(first_numbers[index])
        number_from_second_set = int(second_numbers[index])
        
        # Check if the numbers are different
        if number_from_first_set != number_from_second_set:
            difference_count += 1  # Increment the difference count

    # Check the number of differences
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" otherwise

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
