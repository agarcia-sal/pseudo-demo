import re

def main():
    # Read the input from standard input
    input_path = input().strip()  # Read the input and remove surrounding whitespace
    
    # Normalize the path by ensuring at most one leading slash
    normalized_path = re.sub(r'^/+', '/', input_path)  # Replace multiple leading slashes with a single leading slash
    
    # Print the normalized path to output
    print(normalized_path)

# Start execution by calling the main function
main()
