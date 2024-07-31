def print_8_segment_display(n):
    """Print numbers in an 8-segment display style up to N lines."""
    segments = [
        [" _ ", "| |", "|_|"], # 0
        ["   ", "  |", "  |"], # 1
        [" _ ", " _|", "|_ "], # 2
        [" _ ", " _|", " _|"], # 3
        ["   ", "|_|", "  |"], # 4
        [" _ ", "|_ ", " _|"], # 5
        [" _ ", "|_ ", "|_|"], # 6
        [" _ ", "  |", "  |"], # 7
        [" _ ", "|_|", "|_|"], # 8
        [" _ ", "|_|", " _|"], # 9
    ]
    for i in range(n):
        segment = segments[i]
        for line in segment:
            print(line)
        print()  
n = int(input("Enter the number of lines (N): "))

if n > 0:
    print_8_segment_display(n)
else:
    print("Please enter a positive integer for the number of lines.")
