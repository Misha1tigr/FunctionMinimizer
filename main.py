print("Вітаю у застосунку для мінімізації функцій!")
minimization_type = int(input("Оберіть тип мінімізації: 1-Квайн; 2-Мак-Класки; 3-Вейча: "))
if minimization_type > 3 or minimization_type < 1:
    raise ValueError("Неправильні вхідні дані")
input_quantity = int(input("Введіть кількість входів функції: "))
if input_quantity < 1:
    raise ValueError("Неправильні вхідні дані")
input_naming_type = int(input("Оберіть назви входів: 0-Ввести власноруч, 1-x1x2x3, 2-x3x2x1, 3-abc: "))
input_names = []
if input_naming_type == 0:
    for i in range(input_quantity):
        input_names.append(input("Введіть назву {} входу: ".format(i + 1)))
elif input_naming_type == 1:
    for i in range(input_quantity):
        input_names.append("x" + str(i + 1))
elif input_naming_type == 2:
    for i in reversed(range(input_quantity)):
        input_names.append("x" + str(i + 1))
elif input_naming_type == 3:
    for i in range(input_quantity):
        input_names.append(chr(i + 97))
else:
    raise ValueError("Неправильні вхідні дані")
print(input_names)
