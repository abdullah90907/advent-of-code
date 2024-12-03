def is_safe_report(report):
    """
    Determines if a report is safe based on the given rules.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if differences are all positive (increasing) or all negative (decreasing)
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    
    # Check if all differences are between 1 and 3 inclusive
    are_differences_valid = all(1 <= abs(diff) <= 3 for diff in differences)
    
    # The report is safe if it is entirely increasing or decreasing and has valid differences
    return (is_increasing or is_decreasing) and are_differences_valid

def count_safe_reports(file_path):
    """
    Counts the number of safe reports from a file.
    """
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Skip empty lines
            if line.strip():
                levels = list(map(int, line.strip().split()))
                if is_safe_report(levels):
                    safe_count += 1
    return safe_count

# Read input from input.txt and count safe reports
file_path = "input.txt"
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")