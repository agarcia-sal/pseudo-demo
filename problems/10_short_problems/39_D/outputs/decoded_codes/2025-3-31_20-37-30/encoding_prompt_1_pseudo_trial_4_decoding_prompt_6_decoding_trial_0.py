# Define the main function
def main():
    # Receive input from the user
    first_input = input()
    second_input = input()

    # Split inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize difference counter
    difference_count = 0

    # Compare corresponding elements in both lists
    for index in range(3):  # Loop through indexes 0 to 2
        first_value = int(first_list[index])     # Convert to integer
        second_value = int(second_list[index])    # Convert to integer
        
        # Check if the values are not equal
        if first_value != second_value:
            difference_count += 1   # Increment the difference counter

    # Determine the output based on the difference count
    if difference_count < 3:
        print("YES")  # If less than 3 differences, print YES
    else:
        print("NO")   # If 3 or more differences, print NO

# Execute the main function if script is run as the main program
if __name__ == "__main__":
    main()
