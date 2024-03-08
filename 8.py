def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_str = input("Введите строку: ")
if is_palindrome(input_str):
    print("Это палиндром")
else:
    print("Это не палиндром")