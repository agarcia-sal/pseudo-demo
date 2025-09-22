def main():
    # Read two lines of input representing two sets of numbers
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    first_set = first_input.split()
    second_set = second_input.split()
    
    # Initialize a counter for the number of differences
    difference_count = 0 
    
    # Loop through each set of three values
    for index in range(3):
        # Convert the string values to integers for comparison
        value_from_first_set = int(first_set[index])
        value_from_second_set = int(second_set[index])
        
        # Check if the two values are not equal
        if value_from_first_set != value_from_second_set:
            # Increment the difference counter
            difference_count += 1
            
    # Evaluate the number of differences
    if difference_count < 3:
        # If there are fewer than 3 differences, output "YES"
        print("YES")
    else:
        # If there are 3 or more differences, output "NO"
        print("NO")

# Start the program
main()
