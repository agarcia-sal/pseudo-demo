import re

def main():
    # Read the input from standard input and strip any leading/trailing whitespace
    input_path = input().strip()
    
    # Normalize the path to replace multiple leading slashes with a single leading slash
    normalized_path = re.sub(r'(^/+)+', '/', input_path)
    
    # Print the normalized path to output
    print(normalized_path)

# Start execution by calling the main function
if __name__ == "__main__":
    main()
