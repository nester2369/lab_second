def unique_elements(input_list):
    unique_list = []
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

user_input = input("Введите числа через пробел: ")
numbers = list(map(int, user_input.split()))

print("Уникальные элементы:", unique_elements(numbers))