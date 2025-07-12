from stats import count_words, count_characters


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    num_characters = count_characters(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(num_characters)

main()