def count_words(string_of_words):
    count = 0
    words = string_of_words.split()
    for word in words:
        count += 1
    return count