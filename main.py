# calculator

# add
def add(n1, n2):  # создаем функцию сложения с 2мя параметрами - будущими числами
    return n1 + n2  # в качестве действия прописываем математическое действие


# Substract
def substract(n1, n2):  # создаем функцию вычитания с 2мя параметрами - будущими числами
    return n1 - n2  # в качестве действия прописываем математическое действие


# Multiply
def multiply(n1, n2):  # создаем функцию умножения с 2мя параметрами - будущими числами
    return n1 * n2  # в качестве действия прописываем математическое действие


# Divide
def divide(n1, n2):  # создаем функцию деления с 2мя параметрами - будущими числами
    return n1 / n2  # в качестве действия прописываем математическое действие


operations = {
    # создаем словарь, где key - это знак математического действия (его вдальнейшем будет определять юзер), а value - название прописанной ранее функции
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?:"))  # запрашиваем у юзера 1е число
for symbol in operations:  # выводим все key из словаря, чтобы юзер выбрал следующее действие
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")  # запрашиваем математическое действие у юзера
num2 = int(input("What's the second number?:"))  # запрашиваем у юзера 2е число
calculation_function = operations[
    operation_symbol]  # создаем переменную, в которой из словаря определяется имя функции, согласно выбранному мат.действию
first_answer = calculation_function(num1,
                                    num2)  # создаем переменную, которая подставляет название выбранной функции и в скобках пишем аргументы, которые будут внесены в параметры ранее созданных функций. Необходимая функция с новыми аргументами выполняется через return

print(f"{num1} {operation_symbol} {num2} = {first_answer}")  # выводим результат на экран

operation_symbol = input("Pick another operation: ")  # спрашиваем мат.действие для следующего вычисления
num3 = int(input("What's the next number? "))  # спрашиваем число, участвующее в следующем мат.вычислении
calculation_function = operations[
    operation_symbol]  # опять определяем название функции из словаря, согласно выбору действия юзером
second_answer = calculation_function(first_answer,
                                     num3)  # выводим функцию , но уже аргументы - 1й ответ после 1го вычисления и новое число

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")  # выводим результат на экран

