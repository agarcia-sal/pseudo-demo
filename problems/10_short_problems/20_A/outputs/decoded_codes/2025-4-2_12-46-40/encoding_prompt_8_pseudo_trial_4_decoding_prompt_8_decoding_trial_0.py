import re

def main():
    # Read the input from standard input
    inputPath = input().strip()
    
    # Remove unnecessary path separators using regex to normalize the path
    # The regex replaces multiple leading slashes with a single leading slash
    normalizedPath = re.sub(r'^/+','/', inputPath)
    
    # Print the normalized path to output
    print(normalizedPath)

# Start execution by calling the main function
main()
