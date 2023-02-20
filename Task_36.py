'''
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.
Ввод: 
print_operation_table(lambda x, y: x * y) 

Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''

def get_size():
    rows = int(input("Задайте количество строк: "))
    columns = int(input("Задайте количество столбцов: "))
    print()
    return rows, columns


def select_operation():
    print(f"Сложение -> '1'\nУмножение -> '2'\nВозведение в степень -> '3'\n\
Вычитание -> '4'\nДеление -> '5'\n")
    number_operation = input("Выберите номер необходимой операции: ")
    match number_operation:
        case '1':
            operation = lambda x, y: x + y
            return operation
        case '2':
            operation = lambda x, y: x * y
            return operation
        case '3':
            operation = lambda x, y: x ** y
            return operation
        case '4':
            operation = lambda x, y: x - y
            return operation            
        case '5':
            operation = lambda x, y: x / y
            return operation

def print_operation_table(operation, rows, columns):
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            print(round(operation(row, column), 2), end=" "*3)
        print()

rows, columns = get_size()
print_operation_table(select_operation(), rows, columns)
