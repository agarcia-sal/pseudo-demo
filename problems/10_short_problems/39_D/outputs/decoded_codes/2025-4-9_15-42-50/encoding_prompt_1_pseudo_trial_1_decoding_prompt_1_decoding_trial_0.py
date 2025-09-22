def main():
    # Read the first line of inputs
    first_input = input()
    # Read the second line of inputs
    second_input = input()
    
    # Split the inputs into lists of strings
    fir = first_input.split()
    sec = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current element from string to integer
        num1 = int(fir[index])
        num2 = int(sec[index])
        
        # Check if the two numbers are not equal
        if num1 != num2:
            # Increment the difference counter
            difference_count += 1 
    
    # Check the number of differences
    if difference_count < 3:
        print("YES")  # They differ in less than three positions
    else:
        print("NO")  # They differ in three or more positions

# Start the program
main()
