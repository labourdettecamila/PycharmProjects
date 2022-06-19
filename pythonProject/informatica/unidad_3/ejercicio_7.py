
numbers = []
for number in range(1,101):
    dict = {}
    dict['number'] = number
    if number % 2 == 0:
        dict['type'] = "par"
    else:
        dict['type'] = "impar"
    numbers.append(dict)

print(numbers)
