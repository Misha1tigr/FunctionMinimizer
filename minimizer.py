from prettytable import PrettyTable


def kvain(input_names, function_list, minimization_for):
    minimization_table = PrettyTable()
    minimization_table.header = False

    columns = []
    current_column = []
    for function_row in range(len(function_list[0].values)):
        tags = []
        for function in range(len(function_list)):
            if int(function_list[function].values[function_row]) == minimization_for:
                tags.append(str(function + 1))
                tags.append(";")
        if tags:
            tags.pop(-1)
            current_column_element = []
            for name in range(len(input_names)):
                if int(bin(function_row)[2:].rjust(len(input_names), '0')[name]) == minimization_for:
                    current_column_element.append(input_names[name])
                else:
                    current_column_element.append("!" + input_names[name])
            current_column_element.append("{" + "".join(tags) + "}")
            current_column.append("".join(current_column_element))
    minimization_table.add_column("",current_column)
    minimization_table.align = "l"
    print(minimization_table)


def muck(input_names, function_list, minimization_for):
    pass


def veich(input_names, function_list, minimization_for):
    pass
# bin(~(a-1))  #bitvise invert for a number
# x.header = False #this disables the header
