# Start Program Execution

# Define Main Function: doMain
def do_main():
    # Prompt the user for input and read two lines containing numeric values
    first_sequence = input().split()  # Split the first line of input into a list
    second_sequence = input().split()  # Split the second line of input into a list
    difference_count = 0  # Initialize count of differences

    # Compare Corresponding Values in the Two Sequences
    for index in range(3):  # Loop through indices 0 to 2
        first_value = int(first_sequence[index])  # Convert from firstSequence to integer
        second_value = int(second_sequence[index])  # Convert from secondSequence to integer
        
        # Check if the values differ
        if first_value != second_value:
            difference_count += 1  # Increment difference count if values do not match

    # Determine Output Based on Differences Count
    if difference_count < 3:
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")   # Output NO otherwise

# Execute Main Function When the Program Starts
do_main()
