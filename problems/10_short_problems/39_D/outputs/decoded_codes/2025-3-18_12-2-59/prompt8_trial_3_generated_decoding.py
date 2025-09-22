def main():
    # Get two lines of input from the user
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into lists of strings
    list1 = firstLine.split()
    list2 = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements of the lists to integers
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the two values are different
        if value1 != value2:
            # Increment the difference counter
            differenceCount += 1
    
    # Check the total count of differences
    if differenceCount < 3:
        # If there are less than three differences, output "YES"
        print("YES")
    else:
        # If there are three or more differences, output "NO"
        print("NO")

# Start the program
main()
