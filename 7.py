text = input("Введите предложение: ")

vowels = 0
consonants = 0

for char in text:
    if char.isalpha():
        if char.lower() in "аеёиоуыэюя":
            vowels += 1
        else:
            consonants += 1

print("Количество гласных букв:", vowels)
print("Количество согласных букв:", consonants)