def main():
    # Read the first line of inputs
    firstInput = input()
    
    # Read the second line of inputs
    secondInput = input()
    
    # Split the inputs into lists of strings
    fir = firstInput.split()
    sec = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current element from string to integer
        num1 = int(fir[index])
        num2 = int(sec[index])
        
        # Check if the two numbers are not equal
        if num1 != num2:
            # Increment the difference counter
            differenceCount += 1 
    
    # Check the number of differences
    if differenceCount < 3:
        print("YES")  # They differ in less than three positions
    else:
        print("NO")   # They differ in three or more positions

# Start the program
main()
