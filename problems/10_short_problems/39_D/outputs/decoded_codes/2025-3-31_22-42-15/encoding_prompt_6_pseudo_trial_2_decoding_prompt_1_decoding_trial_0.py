def main():
    # Read two input strings representing test results
    firstTestResults = input()
    secondTestResults = input()
    
    # Split the input strings into lists of strings
    firstTestList = firstTestResults.split()
    secondTestList = secondTestResults.split()
    
    # Initialize a counter to track the number of differences
    differenceCount = 0
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the elements from strings to integers
        firstTestValue = int(firstTestList[index])
        secondTestValue = int(secondTestList[index])
        
        # Check if the values are different
        if firstTestValue != secondTestValue:
            # Increment the difference counter
            differenceCount += 1
            
    # Check the number of differences recorded
    if differenceCount < 3:
        print("YES")  # Less than 3 differences means the tests are similar
    else:
        print("NO")   # 3 or more differences means the tests are different

# Execute the main function
main()
