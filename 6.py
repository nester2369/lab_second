def filter_words_by_letter(word_list, letter):
    result = [word for word in word_list if word.startswith(letter)]
    return result

word_list = input("Введите список слов через пробел: ").split()
letter = input("Введите букву для фильтрации: ")

filtered_words = filter_words_by_letter(word_list, letter)
print(filtered_words)