def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Введите строку: ")
reversed_input = reverse_string(user_input)
print("Обратная строка:", reversed_input)