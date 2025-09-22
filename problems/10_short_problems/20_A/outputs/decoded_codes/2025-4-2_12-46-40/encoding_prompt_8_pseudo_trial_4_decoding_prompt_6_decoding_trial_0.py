import re

def main():
    # Read the input from standard input
    input_path = input().strip()  # Remove any leading or trailing whitespace
    
    # Normalize the path by replacing multiple leading slashes with a single leading slash
    normalized_path = re.sub(r'^/+', '/', input_path)  # Replace multiple leading slashes
    normalized_path = re.sub(r'//+', '/', normalized_path)  # Replace multiple slashes with a single slash elsewhere in the path
    
    # Print the normalized path to output
    print(normalized_path)

# Start execution by calling the main function
main()
