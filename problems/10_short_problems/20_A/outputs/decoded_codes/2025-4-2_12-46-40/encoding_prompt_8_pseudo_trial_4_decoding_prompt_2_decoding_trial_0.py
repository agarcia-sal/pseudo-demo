import re

def main():
    # Read the input from standard input
    inputPath = input().strip()
    
    # Remove leading slashes, ensuring at most one leading slash
    # Using regex to replace multiple leading slashes with a single leading slash
    normalizedPath = re.sub(r'^/+', '/', inputPath)
    
    # Print the normalized path to output
    print(normalizedPath)

# Start execution by calling the main function
main()
