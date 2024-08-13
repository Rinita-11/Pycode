def main():
    input_string = "India is my motherland. I love my country. Capital of India is New Delhi."
    string_length = len(input_string)
    print(f"Length of the string: {string_length}")
    substring = "country"
    if substring in input_string:
        print(f"The substring '{substring}' is found in the string.")
    else:
        print(f"The substring '{substring}' is not found in the string.")

    words = input_string.replace('.', '').replace(',', '').lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("Occurrences of each word:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
