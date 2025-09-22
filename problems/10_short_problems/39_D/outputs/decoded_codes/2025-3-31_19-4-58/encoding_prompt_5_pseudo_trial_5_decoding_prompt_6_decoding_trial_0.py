def main():
    # Read two lines of input from the user, each containing three numbers
    first_set = input()
    second_set = input()

    # Split the input strings into separate numbers
    first_numbers = first_set.split()
    second_numbers = second_set.split()

    # Initialize a count to track the number of differences
    difference_count = 0 

    # Loop through the numbers in the two sets
    for index in range(3):  # From index 0 to 2
        # Convert the current numbers from strings to integers
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])
        
        # Check if the current numbers from both sets are different
        if first_number != second_number:
            # Increment the difference count if they are different
            difference_count += 1
    
    # After comparing all numbers, check the difference count
    if difference_count < 3:
        # If there are fewer than three differences, output "YES"
        print("YES")
    else:
        # If there are three or more differences, output "NO"
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
