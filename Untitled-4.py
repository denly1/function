def sum_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total
number = 12345
result = sum_digits(number)
print("Сумма цифр числа", number, ":", result)