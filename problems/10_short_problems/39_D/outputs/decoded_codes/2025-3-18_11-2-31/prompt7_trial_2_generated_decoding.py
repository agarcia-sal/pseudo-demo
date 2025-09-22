def check_three_values_difference():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()

    # Split the input lines into separate components
    first_values = first_line.split()
    second_values = second_line.split()
    
    # Initialize a counter for discrepancies
    discrepancy_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are different
        if first_value != second_value:
            discrepancy_count += 1

    # Determine the output based on the count of discrepancies
    if discrepancy_count < 3:
        print("YES")
    else:
        print("NO")

# Main program execution entry point
if __name__ == "__main__":
    check_three_values_difference()
