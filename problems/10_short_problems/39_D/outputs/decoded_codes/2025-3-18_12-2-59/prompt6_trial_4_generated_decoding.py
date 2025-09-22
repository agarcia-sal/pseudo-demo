def main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_values = first_line.split()
    second_values = second_line.split()
    
    # Initialize a counter to track the number of different values
    differences_count = 0 
    
    # Iterate through the first three values from both lists
    for index in range(3):
        # Convert current values from strings to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are different
        if first_value != second_value:
            differences_count += 1 
    
    # Check if the number of differences is less than 3
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()
