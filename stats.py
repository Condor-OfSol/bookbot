def count_words(string_of_words):
    count = 0
    words = string_of_words.split()
    for word in words:
        count += 1
    return count

def count_characters(string_of_words):
    characters_count = {}
    for character in string_of_words:
        if character.lower() in characters_count:
            characters_count.update({character.lower(): characters_count[character.lower()] + 1})
        else:
            characters_count[character.lower()] = 1
    return characters_count