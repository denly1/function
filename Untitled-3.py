def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
number = 10
result = is_even(number)
print("Число", number, "является четным?", result)