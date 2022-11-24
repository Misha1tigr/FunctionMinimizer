from prettytable import PrettyTable

print("Вітаю у застосунку для мінімізації функцій!")
minimization_type = int(input("Оберіть тип мінімізації: 1-Квайн; 2-Мак-Класки; 3-Вейча: "))
if minimization_type != 1 and minimization_type != 2 and minimization_type != 3:
    raise ValueError("Неправильні вхідні дані")
function_quantity = int(input("Введіть кількість функцій для мінімізації: "))
if function_quantity < 1:
    raise ValueError("Неправильні вхідні дані")
input_quantity = int(input("Введіть кількість входів функцій: "))
if input_quantity < 1:
    raise ValueError("Неправильні вхідні дані")
input_naming_type = int(input("Оберіть назви входів: 0-Ввести власноруч, 1-x1x2x3, 2-x3x2x1, 3-abc: "))
input_names = []
if input_naming_type == 0:
    for i in range(input_quantity):
        input_names.append(input(f"Введіть назву {i + 1} входу: "))
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


class Function:
    def __init__(self, inputs, values):
        self.inputs = inputs
        self.values = values

    def __str__(self):
        return "Входи: " + " ".join(["{}"] * len(self.inputs)).format(*self.inputs) + \
               "; Значення: " + " ".join(["{}"] * len(self.values)).format(*self.values)


functionList = []
for f in range(function_quantity):
    print(f"Введіть значення {f + 1} функції на усіх наборах через пробіл. "
          "Якщо функція не визначена на наборі ставте мінус(-)")
    output_values = input().split()
    if len(output_values) != pow(2, input_quantity):
        raise ValueError("Ви не ввели усі значення функції")
    for item in output_values:
        if item != "0" and item != "1" and item != "-":
            raise ValueError("Значення функції мають бути лише 0, 1 або -")
    functionList.append(Function(input_names, output_values))
# print(*functionList)  testing
input_table = PrettyTable()
input_table.field_names = functionList[0].inputs + list(f"f{i + 1}" for i in range(function_quantity))
for i in range(pow(2, input_quantity)):
    rowValue = []
    for j in range(function_quantity):
        rowValue.append(functionList[j].values[i])
    input_table.add_row(list(str(bin(i)[2:]).rjust(input_quantity, '0')) + rowValue)
print(input_table)
