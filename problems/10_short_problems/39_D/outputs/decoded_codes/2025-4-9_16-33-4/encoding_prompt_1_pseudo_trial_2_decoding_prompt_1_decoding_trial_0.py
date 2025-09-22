def main():
    # Read two lines of input representing two sets of numbers
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    fir = firstInput.split()
    sec = secondInput.split()
    
    # Initialize a counter for the number of differences
    dif = 0 
    
    # Loop through each set of three values
    for ind in range(3):
        # Convert the string values to integers for comparison
        val1 = int(fir[ind])
        val2 = int(sec[ind])
        
        # Check if the two values are not equal
        if val1 != val2:
            # Increment the difference counter
            dif += 1 
    
    # Evaluate the number of differences
    if dif < 3:
        # If there are fewer than 3 differences, output "YES"
        print("YES")
    else:
        # If there are 3 or more differences, output "NO"
        print("NO")

# Start the program
main()
