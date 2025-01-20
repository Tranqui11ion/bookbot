def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"This book contain {num_words} words")
    print_char_count(get_char_count(text))


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_char_count(text):
    text = text.lower()
    words = text.split()
    char_count = {}
    for word in words:
        for char in word:

            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def print_char_count(char_count):
    for key, value in char_count.items():
        if key not in ".#":
            print(f"The '{key}' character was found {value} times")


main()
