def main():
    input_string = input("Enter a comma-separated sequence of words: ")
    words = input_string.split(',')
    words.sort()
    sorted_string = ','.join(words)
    print("Sorted words:", sorted_string)

if __name__ == "__main__":
    main()
