def square_numbers():
    input_list = list(map(int, input("Введите список чисел через пробел: ").split()))
    squared_list = [num ** 2 for num in input_list]
    return squared_list

print(square_numbers())