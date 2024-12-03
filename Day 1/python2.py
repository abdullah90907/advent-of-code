def calculate_similarity_score(left_list, right_list):
    """
    Calculate similarity score by counting occurrences of left list elements in right list.
    
    Args:
    left_list (list): The first list of numbers
    right_list (list): The second list of numbers
    
    Returns:
    int: Similarity score
    """
    # Count occurrences of each number in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        # Count how many times the number appears in the right list
        occurrences = right_counts.get(num, 0)
        
        # Multiply the left list number by its occurrences in the right list
        similarity_score += num * occurrences
    
    return similarity_score

def read_input_from_file(filename):
    """
    Read input from a file and split into left and right lists.
    
    Args:
    filename (str): Path to the input file
    
    Returns:
    tuple: Two lists of integers (left_list, right_list)
    """
    try:
        with open(filename, 'r') as file:
            left_list = []
            right_list = []
            
            for line in file:
                # Split the line and convert to integers
                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)
            
            return left_list, right_list
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], []
    except ValueError:
        print("Error: Invalid input format. Ensure each line contains two integers separated by a space.")
        return [], []

def main():
    # Specify the input file path
    input_filename = 'input.txt'
    
    # Read input from file
    left_list, right_list = read_input_from_file(input_filename)
    
    # Check if lists are not empty
    if left_list and right_list:
        # Calculate and print the similarity score
        similarity_score = calculate_similarity_score(left_list, right_list)
        print(f"Similarity Score: {similarity_score}")
        
        # Optional: Print some additional information
        print(f"Number of input pairs: {len(left_list)}")
        
        # # Print lists for verification
        # print("\nLeft List:", left_list)
        # print("Right List:", right_list)
        
        # Print detailed breakdown (for the given example)
        if len(left_list) <= 10:  # Only for small lists to keep output readable
            print("\nDetailed Breakdown:")
            right_counts = {}
            for num in right_list:
                right_counts[num] = right_counts.get(num, 0) + 1
            
            for num in left_list:
                occurrences = right_counts.get(num, 0)
                print(f"{num} appears {occurrences} time(s) in right list: {num} * {occurrences} = {num * occurrences}")

# Executable script
if __name__ == "__main__":
    main()